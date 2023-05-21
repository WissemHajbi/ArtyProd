from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from . import forms
from . import models
    
# @login_required
def Home(request):
    projects = models.Project.objects.all()
    services = models.Service.objects.all()
    personnel = models.Personnel.objects.all()
    return render(request,"main.html",{"projects":projects, "services" : services,"personnel" : personnel})


def Register(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, f'{username} : compte a été créé avec succès !')
            return redirect('home')
    else:
        form = forms.UserCreationForm()
    return render(request, 'register.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form  = AuthenticationForm(request)
    return render(request, 'login.html' ,{"form":form})

def Logout(request):
    logout(request)
    return redirect('home')