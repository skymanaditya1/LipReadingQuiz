from django.shortcuts import render, redirect
#from users.forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from users.forms import SignUpForm

# Create your views here.
def dashboard(request):
    return render(request, "users/dashboard.html")

# User registration view 
'''def register(request):
    if request.method == "GET":
        return render(
            request, 
            "users/register.html", 
            {"form": CustomUserCreationForm} # this is the custom user creation form which is rendered by the browser
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user)
            return redirect(reverse("dashboard"))'''

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # save the form 
            user = form.save() 
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            # authenticate the user with his credentials 
            #user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse("dashboard"))
    else:
        form = SignUpFormuser/dashboard/()
    return render(request, 'users/register.html', {'form':form})