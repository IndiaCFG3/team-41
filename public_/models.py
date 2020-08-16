from django.db import models

# Create your models here.

class Scheme(models.Model):
    Name = models.TextField(max_length = 100)
    Description =  models.TextField(max_length = 1000)
    Income_lowerbound = models.IntegerField()
    Income_upperbound = models.IntegerField()
    Gender = models.TextField(max_length = 10)
    Adhar = models.BooleanField(default=True)
    PanCard = models.BooleanField(default=True)