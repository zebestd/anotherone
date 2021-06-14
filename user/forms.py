from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




from .models import Usta, Ilce


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UstaForm(forms.ModelForm):
    class Meta:
        model = Usta
        fields = ('name', 'category', 'il','ilce', 'website', 'email', 'desc', 'telefon')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ilce'].queryset = Ilce.objects.none()
        self.fields['name'].required = True
        self.fields['category'].required = True
        self.fields['il'].required = True
        self.fields['ilce'].required = True
        self.fields['email'].required = True
        self.fields['telefon'].required = True

        for field in self.fields.values():
                    field.error_messages = {'required':'Lutfen bu alani doldurunuz'.format(
                        fieldname=field.label)}


        if 'il' in self.data:
            try:
                il_id = int(self.data.get('il'))
                self.fields['ilce'].queryset = Ilce.objects.filter(il_id=il_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['ilce'].queryset = self.instance.il.ilce_set.order_by('name')