from django.db import models

# Create your models here.

class project(models.Model):
     firstname = models.CharField(max_length=200)
     lastname = models.CharField(max_length=200)
     ids = models.CharField(max_length=300)
     location = models.CharField(max_length=500)
     numconnections = models.IntegerField(max_length=500)
     skills = models.CharField(max_length=3000)
     educations = models.CharField(max_length=3000)
     emailAddress = models.CharField(max_length=300)
     phoneNumbers = models.CharField(max_length=300)

