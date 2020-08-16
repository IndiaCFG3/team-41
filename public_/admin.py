from django.contrib import admin
<<<<<<< HEAD
from . models import Scheme
# Register your models here.

admin.site.register(Scheme)
=======
from public_.models import User,Volunteer,Scheme
# Register your models here.
admin.site.register(User)
admin.site.register(Volunteer)
admin.site.register(Scheme)
>>>>>>> 82396fcfe03c3f54913433f75111ca48386d7bb4
