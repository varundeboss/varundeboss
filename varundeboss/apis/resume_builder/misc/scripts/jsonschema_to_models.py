import sys
import json

class JsonschemaToJsonld(object):

	def __init__(self, json_schema_file):
		f_obj = open(json_schema_file, "r")

		json_schema = eval(f_obj.read(), {"null": None, "true": True, "false": False})

		context = "http://schema.org"
		self.jsonld_tmpl = {
			"@context": context,
			"@type": json_schema["title"],
		}

		self.properties = json_schema.get("properties")
		self.definitions = json_schema.get("definitions")

	def get_value_from_type(self,obj_type, p_key):
		if obj_type:
			if obj_type == "array":
				return [self.definitions.get(p_key, {}).get("title", "")]
			elif obj_type == "string":
				return self.definitions.get(p_key, {}).get("title", "")
			else:
				raise Exception("Object Type: " + obj_type + " not found")

	def get_ref(self):


	def get_jsonschema_from_jsonld(self):
		jsonld_tmpl = self.jsonld_tmpl
		if self.properties:
			for p_key, p_val in self.properties.items():
				obj_type = p_val.get("type")
				ref = p_val.get("$ref", p_val.get("items"))	
				jsonld_tmpl[p_key] = self.get_value_from_type(obj_type, p_key)

		return jsonld_tmpl 					

if __name__ == "__main__":
	js2jld_obj = JsonschemaToJsonld(sys.argv[1])
	jsonld = js2jld_obj.get_jsonschema_from_jsonld()
	import pdb;pdb.set_trace()
	parsed = json.loads(json.dumps(jsonld))
	print(json.dumps(parsed, indent=4, sort_keys=True))
