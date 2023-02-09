from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm





class AdOrderPetTemporarityForm(forms.ModelForm):
    class Meta:
        model = OrderPetTemporarity
        fields = '__all__'


class AdToHomeForm(forms.ModelForm):
    class Meta:
        model = OrderPet
        fields = '__all__'


class AdTransportHelpForm(forms.ModelForm):
    class Meta:
        model = TransportationOrder
        fields = '__all__'


class AdVolOrderForm(forms.ModelForm):
    class Meta:
        model = VolOrder
        fields = '__all__'


class AdFoodMedicinesHelpForm(forms.ModelForm):
    class Meta:
        model = MedicamentosAdd
        fields = '__all__'

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Пользователь', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','password1','password2','email')


class login_UserForm(AuthenticationForm):
    username = forms.CharField(label='Пользователь', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','password1','password2','email')

