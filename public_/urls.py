from django.urls import path
from django.conf.urls import url
from . import views

app_name='public'

urlpatterns = [
   path('user/new/',views.CreateUser.as_view(),name='createuser'),
   path('volunteer/new/',views.CreateVolunteer.as_view(),name='createvolunteer'),

]
