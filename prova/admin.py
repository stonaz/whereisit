from django.contrib.gis import admin
from models import Prova

admin.site.register(Prova, admin.OSMGeoAdmin)
