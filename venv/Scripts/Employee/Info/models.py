from django.db import models

# Create your models here.

class Empdet(models.Model):
    empid = models.IntegerField()
    empname = models.CharField(max_length=100)
    empaddress = models.CharField(max_length=200)
    empsal = models.IntegerField()

