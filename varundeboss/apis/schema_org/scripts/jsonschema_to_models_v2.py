import sys
import os
import json
from glob import glob

class JsonschemaToModelsV2(object):

	def __init__(self):		
		URL_PREFIX = ""
		URL_SUFFIX = ".json"
		INPUT_FILE = "schema.json"
		schema_org_url = "http://schema.org"

		fin_obj = open(INPUT_FILE, "r")

		self.json_schema = eval(fin_obj.read(), {"null": None, "true": True, "false": False})

		self.import_tmpl = """from __future__ import unicode_literals\n\nfrom django.db import models\n\nfrom django.contrib.contenttypes.fields import GenericForeignKey\nfrom django.contrib.contenttypes.models import ContentType\n\n# Create your models here."""
		self.model_tmpl = """\n\nclass %(schema_type)s(models.Model):\n\n"""
		self.django_tmpl = """\t%(property)s = models.%(django_model)s(blank=True, null=True, verbose_name="%(verbose_name)s", help_text='''%(help_text)s''')\n"""
		self.foreign_tmpl = """\t%(property)s = models.ForeignKey('%(foreign_key)s', on_delete=models.CASCADE, verbose_name="%(verbose_name)s", blank=True, null=True, help_text='''%(help_text)s''', related_name="%(related_name)s")\n"""
		self.generic_foreign_tmpl = """\n\tcontent_type = models.ForeignKey(ContentType)\n\tobject_id = models.PositiveIntegerField()\n\tcontent_object = GenericForeignKey('content_type', 'object_id')\n"""
		self.str_tmpl = """\n\tdef __str__(self):\n\t\treturn str(self.id)\n"""
		self.meta_tmpl = """\n\tclass Meta:\n\t\tverbose_name = '%(verbose_name)s'\n\t\tverbose_name_plural = '%(verbose_name_plural)s'\n"""

		self.schema_map = {
			"Boolean": "NullBooleanField",
			"Date": "DateField",
			"Number": "IntegerField",
			"Text": "TextField",
			"URL": "TextField",
			"Time": "TimeField",
			"Integer": "IntegerField",
			"DateTime": "DateTimeField",
			"Float": "FloatField",
		}

		self.to_lower_camel_case = lambda s: s[:1].lower() + s[1:] if s else ''

	def get_model_from_jsonschema(self, schema_type, schema_val, fout_obj):
		fout_obj.write(self.model_tmpl%{"schema_type": schema_type})
		fields = schema_val.get("fields")
		if schema_type in list(self.schema_map.keys()):				
			if fields:
				fout_obj.write(self.django_tmpl%{"property": self.to_lower_camel_case(fields[0]["name"]), "help_text": self.json_schema[fields[0]["name"]]["comment"], "django_model": self.schema_map[schema_type], "verbose_name": fields[0]["name"]})
			else:
				fout_obj.write(self.django_tmpl%{"property": "value", "help_text": schema_val["comment"], "django_model": self.schema_map[schema_type], "verbose_name": "Value"})
		else:
			if fields:
				for field in fields:
					types = field.get("types")
					if types:
						for stype in types:
							fout_obj.write(self.foreign_tmpl%{"property": self.to_lower_camel_case(field["name"] + stype), "help_text": field["comment"], "foreign_key": stype, "verbose_name": field["name"].title(), "related_name": schema_type.lower() + "_" + field["name"].lower() + "_" + stype.lower()})
					else:
						fout_obj.write(self.foreign_tmpl%{"property": self.to_lower_camel_case(field["name"]), "help_text": self.json_schema[field["name"]]["comment"], "foreign_key": field["name"], "verbose_name": field["name"].title(), "related_name": schema_type.lower() + "_" + field["name"].lower()})

		fout_obj.write(self.str_tmpl)
		fout_obj.write(self.meta_tmpl%{"verbose_name": schema_type, "verbose_name_plural": schema_type})

	def get_models_from_jsonschema(self):
		fout_obj = open("../models.py", "w")
		fout_obj.write(self.import_tmpl)

		for schema_type, schema_val in self.json_schema.items():
			self.get_model_from_jsonschema(schema_type, schema_val, fout_obj)

		fout_obj.close()

if __name__ == "__main__":
	js2model_obj = JsonschemaToModelsV2()		
	js2model_obj.get_models_from_jsonschema()