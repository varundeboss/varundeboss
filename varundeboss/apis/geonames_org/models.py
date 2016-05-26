from django.db import models

# Create your models here.

class Country(models.Model):

	name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Country")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Country"
		verbose_name_plural = "Countries"

class Continent(models.Model):

	name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Continent")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Continent"
		verbose_name_plural = "Continents"

class Geoname(models.Model):

	name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Geo Name")
	country = models.ForeignKey(Country, verbose_name="Country")
	continent = models.ForeignKey(Continent, verbose_name="Continent")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Geoname"
		verbose_name_plural = "Geonames"