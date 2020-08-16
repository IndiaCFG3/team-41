from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class membership_status(AbstractUser):
    Name = models.TextField(max_length = 100)
    Receipt_Number = models.AutoField(primary_key=True)
    Date = models.DateField(auto_now_add=True)
    Father_Name = models.TextField(max_length = 100)
    Mother_Nme = models.TextField(max_length = 100)
    Dob = models.DateField()
    Age = models.IntegerField()
    Education = models.TextField(max_length =100)
    Address = models.TextField(max_length = 100)
    City = models.TextField(max_length = 100)
    State = models.TextField(max_length = 100)
    Family_members_count = models.IntegerField()
    Occupation = models.TextField(max_length=100)
    Montly = models.IntegerField()
    Volunteer_id = models.IntegerField(null=True)

class ngo_staff(AbstractUser):
    Name = models.TextField(max_length = 100)
    Enrollment_ID = models.AutoField(primary_key=True)
    DateOfEnrollment = models.DateField(auto_now_add=True)
    Father_Name = models.TextField(max_length = 100)
    Mother_Nme = models.TextField(max_length = 100)
    Dob = models.DateField()
    Age = models.IntegerField()
    Education = models.TextField(max_length =100)
    Address = models.TextField(max_length = 100)
    City = models.TextField(max_length = 100)
    State = models.TextField(max_length = 100)
    Family_members_count = models.IntegerField()
    Occupation = models.TextField(max_length=100)
    Montly = models.IntegerField()
    Volunteer_id = models.IntegerField(null=True)
