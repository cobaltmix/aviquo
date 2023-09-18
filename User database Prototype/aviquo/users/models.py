from django.db import models

# Create your models here.

from django.db import models
class User(models.Model):
  firstname = models.CharField(max_length=255, null=True)
  lastname = models.CharField(max_length=255, null=True)
  password = models.CharField(max_length=128, null=True)