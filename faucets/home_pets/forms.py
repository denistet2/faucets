from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import OrderPetTemporarity





class AdOrderPetTemporarity(ModelForm):
    class Meta:
        model = OrderPetTemporarity
        fields = '__all__'
        widgets = {
            "name": TextInput(attrs={'class': 'form-control',
                                       'placeholder':'Фамилия и имя'}),
            "phone": TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Номер телефона'}),
            "pets": TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Питомец'}),
            "data_order_pet": DateTimeInput(attrs={'class': 'form-control',
                                           'placeholder': 'Дата'}),
            "start_time": DateTimeInput(attrs={'class': 'form-control',
                                           'placeholder': 'Начало'}),

            "end_time": DateTimeInput(attrs={'class': 'form-control',
                                          'placeholder': 'Окончание'}),
            "message": Textarea(attrs={'class': 'form-control',
                                                    'placeholder': 'Замечания'}),
                  }
