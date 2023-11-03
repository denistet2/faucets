from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import *
from django import forms





class AdOrderItemTemporarytyForm(forms.ModelForm):
    class Meta:
        model = OrderItemTemporarity
        fields = '__all__'


class AdToHomeForm(forms.ModelForm):
    class Meta:
        model = OrderItem
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