from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import Usta




from .models import Usta, Ilce




class UstaForm(ModelForm):
    class Meta:
         model = Usta
         fields = ('name', 'category', 'il','ilce', 'website', 'email', 'desc', 'telefon', 'image')


         
    


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']



 