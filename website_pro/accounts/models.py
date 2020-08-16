from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class UserInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(blank=False,max_length=100)
    mobile_no=PhoneNumberField(null=False, blank=False, unique=True)
    user_role=models.CharField(max_length=100,default='user')

    def __str__(self):
        return self.user.username
