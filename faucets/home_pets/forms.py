from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import *
from django import forms





class AdOrderPetTemporarytyForm(forms.ModelForm):
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