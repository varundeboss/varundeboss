from django.db import models

from apis.schema_org.models import Continent, Country

# Create your models here.

class Geoname(models.Model):

	name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Geo Name")
	continent = models.ForeignKey(Continent, verbose_name="Continent")
	country = models.ForeignKey(Country, verbose_name="Country")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Geoname"
		verbose_name_plural = "Geonames"