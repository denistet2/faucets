from django.db import models
from datetime import datetime




class HomePet(models.Model):
    PETS_VAR = [

        (1, 'Собака'),
        (2, 'Кот'),
        (3, 'Птица'),
        (4, 'Насекомое')

    ]
    pets = models.IntegerField('Категория', choices=PETS_VAR, help_text="Вид питомца" )
    foto = models.ImageField(upload_to='images', blank=True, verbose_name='Фото')
    name_pets = models.CharField('Кличка', max_length=20, help_text="Кличка")
    age_pets = models.IntegerField('Возвраст', help_text="Возраст")
    text_about_pets = models.TextField(max_length=200, help_text="Замечания")

    # def __str__(self):
    #     return self.pets, self.name_pets, self.age_pets, self.foto, self.text_about_pets


class HelpList(models.Model):
    help_id = models.CharField(max_length=20, help_text="Enter field documentation")


class OrderHelp(models.Model):
    name = models.CharField(max_length=20, help_text="Имя")
    help_type = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)


class News(models.Model):
    pets = models.CharField(max_length=20, help_text="Enter field documentation")
    text_news = models.TextField(max_length=20, help_text="Enter field documentation")
    data = models.DateTimeField(blank=True, verbose_name="Дата")


class OrderPet(models.Model):
    name = models.CharField(max_length=30, help_text="Фамилия и имя")
    phone = models.CharField(max_length=10, help_text="Номер телефона")
    pets = models.CharField(max_length=20, help_text="Питомец")
    message = models.TextField(max_length=100, help_text="Замечания")
    data_order_pet = models.DateTimeField(verbose_name="Дата")


class OrderPetTemporarity(models.Model):
    name = models.CharField(max_length=30, help_text="Фамилия и имя")
    phone = models.CharField(max_length=10, help_text="Номер телефона")
    pets = models.CharField(max_length=20, help_text="Питомец")
    data_order_pet = models.DateTimeField(verbose_name="Дата")
    start_time = models.DateTimeField(verbose_name="Начало")
    end_time = models.DateTimeField(verbose_name="Окончание")
    message = models.TextField(max_length=100, help_text="Замечания")


class TransportationOrder(models.Model):
    TRANSPORT_VAR = [

     (1, 'Доставка еды, медикаментов и других небольших вещей'),
     (2, 'Доставка сена или соломы, строительных материлов для будок и других крупногабаритных вещей'),
     (3, 'Транспортировка небольших собак и котов'),
     (4, 'Транспортировка больших собак')

    ]
    driver_name = models.CharField(max_length=30, help_text="Инициалы")
    phone_numb = models.CharField(max_length=10, help_text="Телефон")
    transport_type = models.PositiveSmallIntegerField(null=True, choices=TRANSPORT_VAR, editable=False)
    data_order_pet = models.DateTimeField(verbose_name="Дата")
    start_time = models.DateTimeField(verbose_name="Начало")
    end_tame = models.DateTimeField(verbose_name="Окончание")
    message = models.TextField(max_length=100, help_text="Замечания")


class VolOrder(models.Model):

    VOL_VAR = [
     (1, 'Хочу помогать на постоянной основе(расписание можно подобрать так, как будет вам удобно'),
     (2, 'Готов помогать иногда.Хочу выбрать удобное для меня время')
    ]
    name_vol = models.CharField(max_length=30, help_text="Фамилия и имя")
    phone = models.CharField(max_length=10, help_text="Номер телефона")
    vol_type = models.PositiveSmallIntegerField(null=True, verbose_name='vol_type', editable=False, choices=VOL_VAR)
    data_order_pet = models.DateTimeField(verbose_name="Дата")
    start_time = models.DateTimeField(verbose_name="Начало")
    end_time = models.DateTimeField(verbose_name="Окончание")
    message = models.CharField(max_length=100, help_text="Замечания")
