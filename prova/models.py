from django.contrib.gis.db import models

class Prova(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)


    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    where = models.PointField()
    objects = models.GeoManager()

    # Returns the string representation of the model.
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name
