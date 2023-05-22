from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from . import forms
from . import models
    
def Home(request):
    projects = models.Project.objects.all()
    services = models.Service.objects.all()
    personnel = models.Personnel.objects.all()
    return render(request,"main.html",{"projects":projects, "services" : services,"personnel" : personnel})

@login_required(login_url="/home")
def Project_details(request, id):
    project = get_object_or_404(models.Project, id=id)
    return render(request, 'project_details.html', {'project': project})

def Register(request):
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
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
        form = forms.UserRegistrationForm()
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

def Demande_project(request):
    if request.method == "POST":
        form = forms.ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.ProjectForm() 
    return render(request, 'demande_project.html', {'form': form})

def Edit_project(request, id):
    project = get_object_or_404(models.Project, id=id)
    if request.method == "POST":
        form = forms.ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            photo = form.cleaned_data['photo']
            if photo:
                project.photo = photo
            project.save()
            return redirect('home')
    else:
        form = forms.ProjectForm(instance=project)
        return render(request, 'Edit_project.html', {'form': form})
    
def Delete_project(request, id):
    project = get_object_or_404(models.Project, id=id)
    if request.method == "POST":
        project.delete()
        return redirect("home")
    return render(request, "delete_project.html", {"project": project})