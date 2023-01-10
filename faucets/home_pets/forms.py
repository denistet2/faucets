from django import forms
from .models import *





class AdOrderPetTemporarity(forms.ModelForm):
    class Meta:
        model = OrderPetTemporarity
        fields = '__all__'