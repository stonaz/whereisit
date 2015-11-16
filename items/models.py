from django.contrib.auth.models import User
from django.contrib.gis.db import models

from profiles.models import Profile
from categories.models import Category

#class Category(models.Model):
#    name = models.CharField(max_length=50)
#    description = models.CharField(max_length=100)
#    def __unicode__(self):              # __unicode__ on Python 2
#        return self.name
#    class Meta:
#        verbose_name_plural = "Categories"
    
class Item(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    owner= models.ForeignKey(Profile,related_name="sharer")
    category = models.ForeignKey(Category,related_name="category")

    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    #where = models.PointField()
    #objects = models.GeoManager()

    # Returns the string representation of the model.
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name
    
    
    
