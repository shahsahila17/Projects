from django.db import models

# Create your models here.
class Shop(models.Model):
    noc=models.CharField(max_length=100)
    cvv=models.IntegerField()
    acc=models.IntegerField()
    exp=models.TextField()