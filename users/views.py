from django.shortcuts import render, redirect
#from users.forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from users.forms import SignUpForm, UserProfileForm

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Not logged in"
    
    context = {'username' : username}
    return render(request, 'users/dashboard.html', context)

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect(reverse("selection_pages:lipreading-protocol-selection"))
    else:
        form = SignUpForm()
        profile_form = UserProfileForm()

    # This will also handle the case where the form was not valid 
    context = {'form' : form, 'profile_form' : profile_form}
    return render(request, 'users/register.html', context)