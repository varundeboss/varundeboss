from django.contrib import admin

from .models import Geoname

# Register your models here.

class GeonameAdmin(admin.ModelAdmin):
	search_fields = []
	list_filter = []

admin.site.register(Geoname, GeonameAdmin)