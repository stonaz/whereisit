from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    poi =  models.PointField()
    def __unicode__(self):              # __unicode__ on Python 2
        return self.user.username
