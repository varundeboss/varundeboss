from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Text(models.Model):

	text = models.TextField(verbose_name="Text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Text'
		verbose_name_plural = 'Text'


class URL(models.Model):

	uRL = models.TextField(verbose_name="URL")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Url'
		verbose_name_plural = 'Url'


class Time(models.Model):

	time = models.TimeField(verbose_name="Time")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Time'
		verbose_name_plural = 'Time'


class Number(models.Model):

	number = models.IntegerField(verbose_name="Number")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Number'
		verbose_name_plural = 'Number'


class Boolean(models.Model):

	boolean = models.NullBooleanField(verbose_name="Boolean")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Boolean'
		verbose_name_plural = 'Boolean'


class DateTime(models.Model):

	dateTime = models.DateTimeField(verbose_name="DateTime")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Datetime'
		verbose_name_plural = 'Datetime'


class Integer(models.Model):

	integer = models.IntegerField(verbose_name="Integer")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Integer'
		verbose_name_plural = 'Integer'


class Date(models.Model):

	date = models.DateField(verbose_name="Date")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Date'
		verbose_name_plural = 'Date'

class Things(models.Model):

	sameAs = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Sameas", help_text='''URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Freebase page, or official website.''', related_name="thing_sameas")
	potentialAction = models.ForeignKey('Actions', on_delete=models.CASCADE, verbose_name="Potentialaction", help_text='''Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role.''', related_name="thing_potentialaction")
	additionalType = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Additionaltype", help_text='''An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof' attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.''', related_name="thing_additionaltype")
	name = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Name", help_text='''The name of the item.''', related_name="thing_name")
	description = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Description", help_text='''A short description of the item.''', related_name="thing_description")
	alternateName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Alternatename", help_text='''An alias for the item.''', related_name="thing_alternatename")
	url = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Url", help_text='''URL of the item.''', related_name="thing_url")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Thing'
		verbose_name_plural = 'Things'


class Actions(models.Model):

	agent = models.TextField(verbose_name="Agent")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Action'
		verbose_name_plural = 'Actions'

class Persons(models.Model):

	affiliation = models.ForeignKey('Organizations', on_delete=models.CASCADE, verbose_name="Affiliation", help_text='''An organization that this person is affiliated with. For example, a school/university, a club, or a team.''', related_name="person_affiliation")

	def __str__(self):
		return str(self.id)

class Organizations(models.Model):

	telephone = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Telephone", help_text='''The telephone number.''', related_name="organization_telephone")
	faxNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Faxnumber", help_text='''The fax number.''', related_name="organization_faxnumber")

	def __str__(self):
		return str(self.id)