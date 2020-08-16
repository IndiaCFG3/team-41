from django.db import models
from django.urls import reverse
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
import misaka


class User(models.Model):
    Gender_Choice = (
        ('male', 'male'),
        ('female', 'female'),
    )
    Education_choice=(
    ('below_10th','below_10th'),
    ('10th','10th'),
    ('12th','12th'),
    ('Graduation','Graduation'),
    ('Post_Grad','Post_Grad'),
    )
    user_id=models.AutoField(primary_key=True, **options)
    name=models.CharField()
    reciept_no=models.AutoField()
    date=models.DateField(auto_now_add=True)
    father_name=models.CharField()
    mother_name=models.CharField()
    DOB=models.DateField()
    AGE=models.IntegerField()
    Education_qualification=models.CharField(choices=Education_choice)
    Address=models.TextField(max_length=100)
    Number_of_family_members=models.IntegerField()
    occupation=models.CharField()
    montly_income=models.IntegerField()
    gender_choice=models.CharField(choices=Gender_Choice)
    mobile_no=PhoneNumberField(null=False, blank=False, unique=True)
    email=models.EmailField()
    volunteer_ID=models.ForeignKey(Volunteer)
    Document_collected=models.BooleanField(null=True)
    membership=models.BooleanField(null=True)

    def __str__(self):
        return self.user_id

class Volunteer(models.Model):
    Gender_Choice = (
        ('male', 'male'),
        ('female', 'female'),
    )
    Education_choice=(
    ('below_10th','below_10th'),
    ('10th','10th'),
    ('12th','12th'),
    ('Graduation','Graduation'),
    ('Post_Grad','Post_Grad'),
    )
    user_id=models.AutoField(primary_key=True, **options)
    name=models.CharField()
    reciept_no=models.AutoField()
    date=models.DateField(auto_now_add=True)
    father_name=models.CharField()
    mother_name=models.CharField()
    DOB=models.DateField()
    AGE=models.IntegerField()
    Education_qualification=models.CharField(choices=Education_choice)
    Address=models.TextField(max_length=100)
    Number_of_family_members=models.IntegerField()
    occupation=models.CharField()
    gender_choice=models.CharField(choices=Gender_Choice)
    mobile_no=PhoneNumberField(null=False, blank=False, unique=True)
    email=models.EmailField()
    approved=models.BooleanField(default=False)





# Create your models here.

class Scheme(model.Model):
    Name = models.TextField(max_length = 100)
    Description =  models.TextField(max_lenth = 1000)
    Income_lowerbound = models.IntegerField()
    Income_upperbound = models.IntegerField()
    Gender = models.TextField(max_length = 10)
    Adhar = models.BooleanField(initial=True)
    PanCard = models.BooleanField(initial=True)
