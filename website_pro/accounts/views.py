from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . forms import UserRegisterForm,UserProfile
from django.core.mail import send_mail
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form=UserProfile(data=request.POST)
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            # messages.success(request, 'Your account has been created! You are now able to log in')
            send_mail('Registration Successfull','Hello there! This is to notify you that your account has been successfully created!','media06@hushmail.com',[email],
    fail_silently=False)
            return redirect('login.html')
    else:
        form = UserRegisterForm()
        profile_form=UserProfile()
    return render(request, 'register.html', {'form': form,'profile_form':profile_form})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('#'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return HttpResponse("invalid login")
    else:
        return render(request,'login.html')
