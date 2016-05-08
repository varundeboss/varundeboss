import sys
import os
import json

from bs4 import BeautifulSoup
import requests

def schema_json_to_file(schema_type, overwrite=False):
	try:
		URL_PREFIX = ""
		URL_SUFFIX = ".json"
		OUTPUT_DIR = "schema.org"

		file_name = URL_PREFIX + schema_type + URL_SUFFIX

		if not os.path.exists(OUTPUT_DIR):
			os.makedirs(OUTPUT_DIR)
		file_url = os.path.join(OUTPUT_DIR, file_name)

		if not os.path.exists(file_url) or overwrite:			
			f_obj = open(file_url, "w")
			schema_json = schema_type_to_json(schema_type)
			f_obj.write(schema_json)
			f_obj.close()
			# print(file_url, ": Overwrite:", overwrite, ": File Written")
		else:
			pass
			# print(file_url, ": Overwrite:", overwrite, ": File Not Written")

		print(schema_type, ": Success")
	except Exception as e:
		print(schema_type, ":", e)

def schema_type_to_json(schema_type):
	URL_PREFIX = ""
	URL_SUFFIX = ".json"

	schema_org_url = "http://schema.org"
	schema_url = os.path.join(schema_org_url, schema_type)

	html_doc = requests.get(schema_url).text

	soup = BeautifulSoup(html_doc, 'html.parser')

	definitions = soup.findAll("table", { "class": "definition-table" })

	schema_title = soup.findAll("h1", {"class": "page-title"})[0].text.strip()
	schema_comment = soup.findAll("div", {"property": "rdfs:comment"})[0].text.strip()
	schema = {
		'id': URL_PREFIX + schema_title + URL_SUFFIX,
		'title': schema_title,
		'description': schema_comment,
		'format': schema_url,
		'media': {"type": "application/json;profile=" + schema_url},
		"properties": {},
		'instances': {}
	}

	def_count = 0	
	try:
		supertypes = definitions[def_count].findAll("tbody", {"class": "supertype"})		

		supertype_names = soup.findAll("th", {"class": "supertype-name"})
		count = 0
		for supertype in supertypes:		
			supertype_name = supertype_names[count].a.get("href").replace("/", "")
			supertype_url = os.path.join(schema_org_url, supertype_name)
			schema_json_to_file(supertype_name)

			properties = supertype.findAll("tr", {"typeof": "rdfs:Property"})
			for prop in properties:
				properties_dict =  schema["properties"].get(supertype_url, {})
				property_key = prop.find("code", {"property":"rdfs:label"}).a.get("href").replace("/", "")
				property_url = os.path.join(schema_org_url, property_key)
				# schema_json_to_file(property_key)
				
				expected_types = [expected_type.nextSibling.get("href").replace("/", "") for expected_type in prop.findAll("link", {"property": "rangeIncludes"})]
				for expected_type in expected_types:schema_json_to_file(expected_type)
				expected_types_url = [os.path.join(schema_org_url, expected_type) for expected_type in expected_types]
				properties_dict[property_url] = {
					"expected_type": expected_types_url,
					"description": " ".join(prop.find("td", {"property": "rdfs:comment"}).text.replace("\n","").split()),
				}
				
				schema["properties"][supertype_url] = properties_dict
			count += 1			
		def_count += 1 if supertypes else def_count
	except Exception as e:
		pass
	
	try:
		instances = definitions[def_count].findAll("tr")
		for instance in instances[1:]:
			instance_key = instance.find("code").a.get("href").replace("/", "")
			instance_url = os.path.join(schema_org_url, instance_key)
			# schema_json_to_file(instance_key)

			instance_used_types = [used_type.a.get("href").replace("/", "") for used_type in instance.findAll("td", {"class": "prop-ect"})]
			for instance_used_type in instance_used_types: schema_json_to_file(instance_used_type)
			instance_used_types_url = [os.path.join(schema_org_url, instance_used_type) for instance_used_type in instance_used_types]
			schema["instances"][instance_url] = {
				"used_on_types": instance_used_types_url,
				"description": " ".join(instance.find("td", {"class": "prop-desc"}).text.replace("\n","").split()),
			}
	except Exception as e:
		pass

	return json.dumps(schema)

if __name__ == "__main__":
	schema_json = schema_json_to_file(sys.argv[1])
	# print schema_json