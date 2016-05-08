import sys
import os
import json
from glob import glob

class JsonschemaToModels(object):

	def __init__(self, schema_type):		
		URL_PREFIX = ""
		URL_SUFFIX = ".json"
		OUTPUT_DIR = "schema.org"
		schema_org_url = "http://schema.org"

		self.schema_type = schema_type
		self.schema_url = os.path.join(schema_org_url, self.schema_type)

		json_schema_file = os.path.join(OUTPUT_DIR, URL_PREFIX + self.schema_type + URL_SUFFIX)
		f_obj = open(json_schema_file, "r")

		self.json_schema = eval(f_obj.read(), {"null": None, "true": True, "false": False})

		context = "http://schema.org"
		self.jsonld_tmpl = {
			"@context": context,
			"@type": self.json_schema["title"],
		}
		self.import_tmpl = """from __future__ import unicode_literals\n\nfrom django.db import models\n\nfrom django.contrib.contenttypes.fields import GenericForeignKey\nfrom django.contrib.contenttypes.models import ContentType\n\n# Create your models here."""
		self.model_tmpl = """\n\nclass %(schema_type)s(models.Model):\n\n"""
		self.property_tmpl = """\t%(property)s = models.ForeignKey(%(foreign_key)s, on_delete=models.CASCADE, verbose_name="%(verbose_name)s", help_text="%(help_text)s")\n"""
		self.foreign_tmpl = """\t%(property)s = models.ForeignKey(%(foreign_key)s, on_delete=models.CASCADE, verbose_name="%(verbose_name)s")\n"""
		self.generic_foreign_tmpl = """\n\tcontent_type = models.ForeignKey(ContentType)\n\tobject_id = models.PositiveIntegerField()\n\tcontent_object = GenericForeignKey('content_type', 'object_id')\n"""
		self.str_tmpl = """\n\tdef __str__(self):\n\t\treturn self.id\n"""
		self.meta_tmpl = """\n\tclass Meta:\n\t\tverbose_name = '%(verbose_name)s'\n\t\tverbose_name_plural = '%(verbose_name_plural)s'\n"""

		self.properties = self.json_schema.get("properties")
		self.instances = self.json_schema.get("instances")

		self.downCase = lambda s: s[:1].lower() + s[1:] if s else ''

	def get_ref(self):
		pass

	def get_model_from_jsonschema(self):
		model_tmpls = {}
		if self.properties:		
			properties = self.properties			
			model_tmpl = self.model_tmpl%{"schema_type": self.schema_type}
			parent_property = properties.pop(self.schema_url) if self.schema_url in properties else {}
			for prop_key, prop_val in parent_property.items():
				prop_name = os.path.split(prop_key)[1]
				if len(prop_val["expected_type"]) <= 1:					
					property_tmpl = self.property_tmpl%{"property": prop_name,\
									"verbose_name": prop_name.title(),\
									"help_text": prop_val["description"],\
									"foreign_key": os.path.split(prop_val["expected_type"][0])[1]}
					model_tmpl += property_tmpl					

			for prop_key in properties:
				prop_name = os.path.split(prop_key)[1]
				model_tmpl += self.foreign_tmpl%{"property": self.downCase(prop_name),\
							  "foreign_key": prop_name,\
							  "verbose_name": prop_name}					

			model_tmpl += self.generic_foreign_tmpl
			model_tmpl += self.str_tmpl
			model_tmpl += self.meta_tmpl%{"verbose_name": self.schema_type.title(),\
						   "verbose_name_plural": self.schema_type.title()}
			model_tmpls[self.schema_type] = model_tmpl
		else:
			print(self.schema_type)
		return model_tmpls

if __name__ == "__main__":
	import_tmpl = """from __future__ import unicode_literals\n\nfrom django.db import models\n\nfrom django.contrib.contenttypes.fields import GenericForeignKey\nfrom django.contrib.contenttypes.models import ContentType\n\n# Create your models here."""
	schema_types = [fpath.split("/")[-1].replace(".json", "") for fpath in glob("schema.org/*.json")]
	model_obj = open("models.py", "w")
	model_obj.write(import_tmpl)
	for schema_type in schema_types:
		js2model_obj = JsonschemaToModels(schema_type)
		model_tmpls = js2model_obj.get_model_from_jsonschema()
		for schema_type in model_tmpls:
			model_obj.write(model_tmpls[schema_type])
	model_obj.close()
