from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import Registeration, normaluser, adminuser
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'enroll/home.html')


def register(request):
    if request.method == "POST":
        fm = Registeration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Registration Successfull !!")
    else:
        fm = Registeration()
    return render(request, 'enroll/register.html', {'form': fm})


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request, request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')


def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = None
            if request.user.is_superuser:
                fm = adminuser(data=request.POST, instance=request.user)
                if fm.is_valid():
                    fm.save()
                    messages.success(
                        request, "Profile updated successfully !!")
            else:
                fm = normaluser(data=request.POST, instance=request.user)
                if fm.is_valid():
                    fm.save()
                    messages.success(
                        request, 'Profile updated successfully !!')
        else:
            if request.user.is_superuser:
                user = User.objects.all()
                fm = adminuser(instance=request.user)
            else:
                fm = normaluser(instance=request.user)
                user = None
        return render(request, 'enroll/profile.html', {'form': fm, 'users': user})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def passchange(request):
    if request.user.is_superuser:
        if request.method == "POST":
            fm = PasswordChangeForm(request.user, request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Password Changed Successfully!!!")
                update_session_auth_hash(request, request.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(request.user)
        return render(request, 'enroll/changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')


def passchange1(request):
    if request.user.is_superuser:
        user = request.user
        if request.method == "POST":
            if request.user.is_superuser:
                pass
            else:
                fm = SetPasswordForm(request.user, request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Password Changed Successfully!!!")
                update_session_auth_hash(request, request.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(request.user)
        return render(request, 'enroll/changepass1.html', {'form': fm, 'user': user})
    else:
        return HttpResponseRedirect('/login/')


def userdetail(request, id):
    if request.user.is_superuser:
        user = User.objects.get(pk=id)
        if request.method == "POST":
            fm = UserChangeForm(data=request.POST, instance=user)
            if fm.is_valid():
                fm.save()
                messages.success(request, "User data updated successfully !!")
        else:
            fm = UserChangeForm(instance=user)
            user = None
        return render(request, 'enroll/userdetail.html', {'form': fm, 'user': user})
    else:
        return HttpResponseRedirect('/login/')
