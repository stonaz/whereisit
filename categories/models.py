from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name
    class Meta:
        verbose_name_plural = "Categories"
