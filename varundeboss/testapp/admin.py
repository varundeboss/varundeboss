from django.contrib import admin

# Register your models here.

from .models import Things, Actions, Persons, Organizations, Text

admin.site.register(Things)
admin.site.register(Actions)
admin.site.register(Persons)
admin.site.register(Organizations)
admin.site.register(Text)