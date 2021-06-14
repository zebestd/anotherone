from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Usta, Ilce
from .forms import UstaForm, CreateUserForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('usta_changelist')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Basariyla kayit oldunuz ' + user + '. Devam etmek icin lutfen giris yapin.')

                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('usta_changelist')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                    login(request, user)
                    return redirect('usta_changelist')
            else:
                messages.info(request, 'kullanici adi VEYA parolayi yanlis girdiniz')
        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


class UstaListView(ListView):
    model = Usta
    form_class = UstaForm
    context_object_name = 'usta'


class UstaCreateView(CreateView):
    model = Usta
    form_class = UstaForm
    success_url = reverse_lazy('usta_changelist')


class UstaUpdateView(UpdateView):
    model = Usta
    form_class = UstaForm
    success_url = reverse_lazy('usta_changelist')


def load_ilce(request):
    il_id = request.GET.get('il')
    ilce = Ilce.objects.filter(il_id=il_id).order_by('name')
    return render(request, 'user/ilce_dropdown_list_options.html', {'ilce': ilce})
