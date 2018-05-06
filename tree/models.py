from django.db import models
from django.contrib import admin
# Create your models here.


class Zone(models.Model):
    zone_id = models.IntegerField()
    name = models.CharField(max_length=100)


admin.site.register(Zone)