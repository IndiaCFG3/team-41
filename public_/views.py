from django.shortcuts import render
from django.views import generic
from public_.models import User,Volunteer,Scheme

# Create your views here.
class CreateUser(generic.CreateView):
    fields= ('name','father_name','mother_name','AGE','DOB','Education_qualification','Number_of_family_members','occupation','gender_choice','montly_income','mobile_no','email')
    model=User

class CreateVolunteer(generic.CreateView):
    fields= ('name','father_name','mother_name','AGE','DOB','Education_qualification','Number_of_family_members','occupation','gender_choice','mobile_no','email')

    model=Volunteer
