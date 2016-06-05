import sys

def get_schemastypes_from_schematype(json_schema, schematype):
	schemastypes = []
	
	if schematype not in schemastypes:
		schemastypes.append(schematype)
		schema = json_schema[schematype]
		for field in schema.get("fields", {}):
			types = field.get("types", {})
			if not types:
				schemastypes.extend(get_schemastypes_from_schematype(json_schema, field["name"]))
			else:
				for stype in types:
					schemastypes.extend(get_schemastypes_from_schematype(json_schema, stype))

	return schemastypes

if __name__ == "__main__":
	all_schema_list = []
	fin_obj = open("schema.json", "r")
	json_schema = eval(fin_obj.read(), {"null": None, "true": True, "false": False})
	for schema_type, schema_val in json_schema.items():
		count = 0
		for field in schema_val.get("fields",{}):
			count += len(field.get("types", [1]))
		if count > 50:
			print(schema_type, count)
	# all_schema_list = get_schemastypes_from_schematype(json_schema, sys.argv[1])

	# print(list(set(all_schema_list)))