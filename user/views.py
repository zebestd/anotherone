from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Usta, Ilce
from .forms import UstaForm, CreateUserForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Basariyla kayit oldunuz ' +
                             user + '. Devam etmek icin lutfen giris yapin.')

            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('usta')
        else:
            messages.info(
                request, 'kullanici adi VEYA parolayi yanlis girdiniz')
    context = {}
    return render(request, 'login.html', context)



@login_required(login_url='login')
def profile(request):
    return render(request, 'user.html')




def logoutUser(request):
    logout(request)
    return redirect('login')


def createUsta(request):
    form = UstaForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = UstaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'form.html', context)

def ustalist(request):
    usta = Usta.objects.all()
    return render(request, 'home.html', {'usta': usta})
    

def home(request):
    context = {}
    return render(request, 'home.html', context)


def load_ilce(request):
    il_id = request.GET.get('il')
    ilce = Ilce.objects.filter(il_id=il_id).order_by('name')
    return render(request, 'user/ilce_dropdown_list_options.html', {'ilce': ilce})
