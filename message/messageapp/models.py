from django.db import models


# Create your models here.

class Msg(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    email = models.CharField(max_length=50)