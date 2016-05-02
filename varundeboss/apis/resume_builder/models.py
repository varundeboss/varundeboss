from __future__ import unicode_literals

from django.db import models

from uuid import uuid4

# Create your models here.

class Resume(models.Model):

	resume_id = models.UUIDField(default=uuid4, unique=True, db_index=True, primary_key=True, verbose_name="Resume ID")
	name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Resume Name")

	experience_level = models.CharField(max_length=100, blank=False, null=False, verbose_name="Experience Level")
	career_field = models.CharField(max_length=100, blank=False, null=False, verbose_name="Career Field")
	career_sub_field = models.CharField(max_length=100, blank=False, null=False, verbose_name="Career Sub-Field")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Resume"
		verbose_name_plural = "Resumes"

		# unique_together = ('user', 'name',)