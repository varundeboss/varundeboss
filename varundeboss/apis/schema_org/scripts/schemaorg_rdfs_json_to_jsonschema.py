import pprint
import json

class SchemaOrgToJsonSchema(object):
	"""docstring for SchemaOrgToJsonSchema"""
	def __init__(self, args=[], kwargs={}):
		super(SchemaOrgToJsonSchema, self).__init__()
		self.args = args
		self.tocamelCase = lambda s: s[:1].lower() + s[1:] if s else ''
		self.schema_rdfs_json = eval(open(kwargs.get("schema_rdfs_json_file")).read(),\
									 {"null": None, "true": True, "false": False})

		self.json_schema = {}

	def get_field(self, schema_dict, superclass):
		if not schema_dict.get("schema:supersededBy"):
			field = {
						# "name": self.tocamelCase(superclass["@id"].replace("schema:", "")),
						"name": superclass["@id"].replace("schema:", ""),
						# "label": superclass.get("rdfs:label", ""),
						"comment": superclass.get("rdfs:comment", "")					
					}

			ranges = schema_dict.get("schema:rangeIncludes")
			if ranges:
				if type(ranges) == type([]):
					field["types"] = [srange["@id"].replace("schema:", "") for srange in ranges]	
				else:
					field["types"] = [ranges["@id"].replace("schema:", "")]
			return field
		return {}

	def get_fields(self, schema_dict, superclasses):
		fields = []
		if type(superclasses) == type([]):						
			for superclass in superclasses:
				field = self.get_field(schema_dict, superclass)
				if field:
					fields.append(field)
		else:
			field = self.get_field(schema_dict, superclasses)
			if field:
				fields.append(field)
		return fields

	def add_fields(self, schema_id, sfields, fields):
		if sfields:
			self.json_schema[schema_id]["fields"].extend(fields)
		else:
			self.json_schema[schema_id]["fields"] = fields[:]

	def set_schema(self, schema_id):
		if not self.json_schema.get(schema_id):
			self.json_schema[schema_id] = {}

	def add_enum(self, schema_id, enum_val):
		enum_list = self.json_schema[schema_id].get("enum")
		if enum_list:
			self.json_schema[schema_id]["enum"].append(enum_val)
		else:
			self.json_schema[schema_id]["enum"] = [enum_val]

	def generate_from_type(self, schema_dict, stype):
		if stype == "rdfs:Class":
			schema_id = schema_dict["@id"].replace("schema:", "")
			self.set_schema(schema_id)
			self.json_schema[schema_id]["comment"] = schema_dict["rdfs:comment"]
			# self.json_schema[schema_id]["label"] = schema_dict["rdfs:label"]

			superclasses = schema_dict.get("rdfs:subClassOf")
			if superclasses:				
				fields = self.get_fields(schema_dict, superclasses)
				sfields = self.json_schema[schema_id].get("fields")
				self.add_fields(schema_id, sfields, fields)

		elif stype == "rdf:Property":
			fields = self.get_fields(schema_dict, schema_dict)
			domains = schema_dict.get("schema:domainIncludes")
			if domains:				
				if type(domains) == type([]):
					for domain in domains:
						schema_id = domain["@id"].replace("schema:", "")
						self.set_schema(schema_id)
						sfields = self.json_schema[schema_id].get("fields")
						self.add_fields(schema_id, sfields, fields)					
				else:
					schema_id = domains["@id"].replace("schema:", "")
					self.set_schema(schema_id)
					sfields = self.json_schema[schema_id].get("fields")
					self.add_fields(schema_id, sfields, fields)
				
		elif stype.startswith("schema:"):
			schema_id = stype.replace("schema:", "")
			self.set_schema(schema_id)
			if schema_dict["@id"].startswith("schema"):
				self.add_enum(schema_id, schema_dict["@id"].replace("schema:", ""))
		else:
			raise Exception("Type not found: " + stype)

	def generate_schema_json(self, schema_dict):
		stypes = schema_dict["@type"]
		if type(stypes) == type([]):
			for stype in stypes:
				self.generate_from_type(schema_dict, stype)
		else:
			self.generate_from_type(schema_dict, stypes)

	def main(self):
		for schema_dict in self.schema_rdfs_json["@graph"]:
			self.generate_schema_json(schema_dict)

		print(json.dumps(self.json_schema))
		# for i in self.json_schema:
		# 	if i == "FinancialService":
		# 		print(i, " : ")
		# 		print(pprint.pformat(self.json_schema[i]))
		# 		prop_list = []
		# 		for j in self.json_schema[i]["fields"]:
		# 			prop_list.append(j["name"])
		# 		prop_list.sort()
		# 		print(prop_list)
		# 		print(len(self.json_schema[i]["fields"]))
		# for i in self.json_schema:
		# 	for j in self.json_schema[i]["fields"]:
		# 		if "types" not in j.keys():
		# 			print(j)
		# print(len(self.json_schema))

if __name__ == "__main__":
	schema_rdfs_json_file = "schema.org-docs-schema_org_rdfa.json"
	stjObj = SchemaOrgToJsonSchema(args=[], kwargs={"schema_rdfs_json_file" : schema_rdfs_json_file})
	stjObj.main()