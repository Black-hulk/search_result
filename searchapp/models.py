from django.db import models

# Create your models here.
class Searchitem(models.Model):
    name=models.CharField(max_length=300)
    detail=models.TextField(max_length=500)


class Searchrecord(models.Model):
    skeyword=models.CharField(max_length=500)
    stime=models.TimeField(auto_now=True)
    sresult=models.CharField(max_length=500)