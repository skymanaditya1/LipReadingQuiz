# users/forms.py 

from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import UserProfile

'''class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.Fields + ("email",)'''

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required a valid email address')

    class Meta:
        model = User 
        fields = (
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2',
        )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'age', 
            'gender', 
            'education', 
            'parents_education', 
            'hearing_loss_age',
            'hearing_loss_intensity',
            'hearing_impairment_type',
            'hearing_aid_type',
            'preferred_mode_of_communication',
            'lipreading_expertise',
        )