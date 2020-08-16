from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from . import views

app_name='accounts'

urlpatterns = [
 path('login/',views.user_login,name='login'),
 path('logout/',auth_views.LogoutView.as_view(),name='logout'),
 path('signup/',views.register,name="signup"),
 path('reset-password/',PasswordResetView.as_view(),name='reset_password'),
 path('reset-password/done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
 url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
 path('reset-password/complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
