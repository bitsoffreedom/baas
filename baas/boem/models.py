from django.db import models
# from django.contrib.gis.geoip import GeoIP
#
# g = GeoIP()

# Create your models here.
class TempMail(models.Model):
    mailfrom = models.EmailField()
    mailsubj = models.CharField(max_length=20)
    mailrcvd = models.DateTimeField()
    mailhdrs = models.CharField()

class SavedMail(models.Model):
    mailrcvd = models.DateTimeField()
    mailhdrs = models.CharField()
    organization = models.ForeignKey('Organization')

class Organization(models.Model):
    emailsuffix = models.CharField(max_length=255)

class Follower(models.Model):
    email = models.EmailField()