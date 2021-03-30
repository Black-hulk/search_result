from django.db import models

# Create your models here.
class Users(models.Model):
    fullname=models.CharField(max_length=50)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=100)