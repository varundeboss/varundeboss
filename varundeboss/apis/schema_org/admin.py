from django.contrib import admin

from .models import Thing, Country, Continent, AdministrativeArea, Landform, Place, Text

# Register your models here.

admin.site.register(Thing)
admin.site.register(Country)
admin.site.register(Continent)
admin.site.register(AdministrativeArea)
admin.site.register(Landform)
admin.site.register(Place)

admin.site.register(Text)