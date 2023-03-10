from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator




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
    age_pets = models.IntegerField('Возраст', help_text="Возраст")
    text_about_pets = models.TextField('Кратко о питомце',max_length=200, help_text="Замечания")

    def __str__(self):
        return self.pets

    class Meta:
        verbose_name='Питомцы'

class HelpList(models.Model):
    help_id = models.CharField(max_length=20, help_text="Enter field documentation")


class OrderHelp(models.Model):
    name = models.CharField('Волонтер',max_length=20, help_text="Имя")
    help_type = models.CharField(max_length=10)
    email = models.EmailField()
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField('Телефон', validators=[phoneNumberRegex], max_length=16, unique=True)



class News(models.Model):
    foto = models.ImageField(upload_to='images', blank=True, verbose_name='Фото')
    text_news = models.TextField(max_length=250, help_text="Enter field documentation")
    data = models.DateTimeField(blank=True, verbose_name="Дата")


class OrderPet(models.Model):
    name = models.CharField('Заводчик', max_length=30, help_text="Фамилия и имя")
    # phone = models.CharField(max_length=10, help_text="Номер телефона")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField('Телефон',validators=[phoneNumberRegex], max_length=16, unique=True)
    pets = models.CharField('Кличка',max_length=20, help_text="Питомец")
    message = models.TextField('Замечания',max_length=100, help_text="Замечания")
    order_data = models.DateTimeField(verbose_name="Дата")


class OrderPetTemporarity(models.Model):
    name = models.CharField('Волонтер',max_length=30, help_text="Фамилия и имя")
    # phone = models.CharField(max_length=10, help_text="Номер телефона")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField('Телефон',validators=[phoneNumberRegex], max_length=16, unique=True)
    pets = models.CharField('Кличка',max_length=20, help_text="Питомец")
    order_data = models.DateTimeField(verbose_name="Дата")
    start_time = models.DateTimeField(verbose_name="Начало")
    end_time = models.DateTimeField(verbose_name="Окончание")
    message = models.TextField('Замечания',max_length=100, help_text="Замечания")


class TransportationOrder(models.Model):
    TRANSPORT_VAR = [

     (1, 'Доставка еды, медикаментов и других небольших вещей'),
     (2, 'Доставка сена или соломы, строительных материлов для будок и других крупногабаритных вещей'),
     (3, 'Транспортировка небольших собак и котов'),
     (4, 'Транспортировка больших собак')

    ]
    driver_name = models.CharField('Перевозчик', max_length=30, help_text="Инициалы")
    # phone_numb = models.CharField(max_length=10, help_text="Телефон")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField('Телефон', validators=[phoneNumberRegex], max_length=16)
    transport_type = models.IntegerField('Вид перевозки', null=True, choices=TRANSPORT_VAR)
    order_data = models.DateTimeField(verbose_name="Дата")
    start_point = models.CharField(max_length=30,verbose_name="Погрузить")
    end_point = models.CharField(max_length=30,verbose_name="Выгрузить")
    message = models.TextField('Замечания', max_length=100, help_text="Замечания")


class VolOrder(models.Model):

    VOL_VAR = [
     (1, 'Хочу помогать на постоянной основе(расписание можно подобрать так, как будет вам удобно'),
     (2, 'Готов помогать иногда.Хочу выбрать удобное для меня время')
    ]
    name_vol = models.CharField('Волонтер', max_length=30, help_text="Фамилия и имя")
    # phone = models.CharField(max_length=10, help_text="Номер телефона")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)
    vol_type = models.IntegerField(null=True, verbose_name='vol_type', choices=VOL_VAR)
    data_order = models.DateTimeField(verbose_name="Дата")
    start_time = models.DateTimeField(verbose_name="Начало")
    end_time = models.DateTimeField(verbose_name="Окончание")
    message = models.CharField(max_length=100, help_text="Замечания")

class MedicamentosAdd(models.Model):

    MEDICAMENTOS_VAR = [
        (1, 'цефтриаксон'),
        (2, 'новокаин'),
        (3, 'гискан'),
        (4, 'гамавит'),
        (5, 'катозал'),
        (6, 'антитокс'),
        (7, 'фоспренил'),
        (8, 'энтеросгель'),
        (9, 'препараты от глистов'),
        (10, 'препараты от блох,клещей'),
        (11, 'для заживления ран')
    ]
    med_type = models.IntegerField('Препарат', choices=MEDICAMENTOS_VAR)
    med_weight = models.IntegerField()
    name = models.CharField('Волонтер',max_length=30, help_text="Фамилия и имя")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField('Телефон', validators=[phoneNumberRegex], max_length=16, unique=True)


class ForageAdd(models.Model):

    FORAGE_VAR = [
        (1, 'крупы'),
        (2, 'Сухие корма'),
        (3, 'Влажные корма'),
        (4, 'Фарш для собак')

    ]
    forage_type = models.IntegerField(null=True, verbose_name='Вид корма', choices=FORAGE_VAR)
    forage_weight = models.IntegerField()
    name = models.CharField('Волонтер',max_length=30, help_text="Фамилия и имя")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField('Телефон', validators=[phoneNumberRegex], max_length=16, unique=True)

class ItemAdd(models.Model):

    ITEM_VAR = [
        (1, 'Ошейники, поводки, намордники'),
        (2, 'Опилки и солома'),
        (3, 'Посуда'),
        (4, 'Теплые вещи'),
        (5, 'Будки')

    ]
    item_type = models.IntegerField(null=True, verbose_name='Категория', choices=ITEM_VAR)
    item_qty = models.IntegerField()
    which_item = models.CharField('Вещь', max_length=100, help_text="Замечания")
    name = models.CharField('Волонтер',max_length=30, help_text="Фамилия и имя")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField('Телефон', validators=[phoneNumberRegex], max_length=16, unique=True)




