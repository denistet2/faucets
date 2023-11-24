from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import *
from django import forms

# class SubRubricForm(forms.ModelForm):
#     super_rubric = forms.ModelChoiceField(
#         queryset=SuperRubric.objects.all(),empty_label=None,
#         label='Надрубрика', required=True)
#
#     class Meta:
#         model = SubRubric
#         fields = '__all__'

#
class AdFavoritesList(forms.ModelForm):
    class Meta:
        model = Favorites
        fields = '__all__'
#
#
class AdBasketForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'
