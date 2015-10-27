from django.contrib.gis import admin
from models import Item,Category

admin.site.register(Category, admin.OSMGeoAdmin)
admin.site.register(Item, admin.OSMGeoAdmin)
