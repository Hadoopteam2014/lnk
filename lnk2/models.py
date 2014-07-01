from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class UserProfile2(models.Model):
    user = models.ForeignKey(User)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    cid = models.CharField(max_length=300)
