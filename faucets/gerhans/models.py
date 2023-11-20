from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator




class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, unique=True, verbose_name='Название')
    order = models.SmallIntegerField(default=0, db_index=True, verbose_name='Порядок')
    super_rubric = models.ForeignKey('SuperRubric', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Надрубрика')

class SuperRubricManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_rubric_isnull=True)

class SuperRubric(Rubric):
    object = SuperRubricManager()
    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        ordering = ('order', 'name')
        verbose_name = 'Надрубрика'
        verbose_name_plural = 'Надрубрики'

class Product(models.Model):
    Product_category = [

        (1, 'Faucet'),
        (2, 'Basin'),
        (3, 'Accessory'),
        (4, 'Gardeneqm')
    ]
    name = models.CharField('Наименование', blank=True, max_length=30, help_text="Артикул")
    categories = models.PositiveSmallIntegerField('Категория',choices=Product_category, help_text="Артикул")
    sku = models.CharField('Артикул', blank=True, max_length=20, help_text="Артикул")
    upc = models.CharField('UPC', blank=False, max_length=20, help_text="Внутренний код")
    ean = models.CharField('EAN', blank=True, max_length=20, help_text="Штрихкод")
    jan = models.CharField('JAN', blank=True, max_length=20, help_text="Артикул")
    isbn = models.CharField('ISBN', blank=True, max_length=20, help_text="Артикул")
    mpn = models.CharField('MPN', blank=True, max_length=20, help_text="Артикул")
    location = models.CharField('Размещение', blank=True, max_length=20, help_text="Артикул")
    quantity = models.CharField('Количество', blank=True, max_length=20, help_text="Артикул")
    model = models.CharField('Модель', blank=True, max_length=20, help_text="На упаковке")
    manufacturer = models.CharField('Производитель', blank=True, max_length=20, help_text="Артикул")
    image_name = models.CharField('Изображение', blank=True, max_length=20, help_text="фото")
    foto = models.ImageField(upload_to='images', blank=True, verbose_name='Изображение')
    shipping = models.CharField('Пересылка', blank=True, max_length=20, help_text="Артикул")
    price = models.DecimalField('Цена', blank=True, help_text="Цена", max_digits=8, decimal_places=2)
    points = models.CharField('Баллы', blank=True, max_length=20, help_text="Артикул")
    date_added = models.DateTimeField('Дата добавления', auto_now_add=True, db_index=True)
    date_modified = models.DateTimeField('Дата изменений', auto_now_add=True, db_index=True)
    date_available = models.DateTimeField('Дата поступления', auto_now_add=True, db_index=True)
    weight = models.CharField('Вес', blank=True, max_length=20, help_text="Артикул")
    weight_unit = models.CharField('Вес нетто', blank=True, max_length=20, help_text="Артикул")
    length = models.CharField('Длина', blank=True, max_length=20, help_text="Артикул")
    width = models.CharField('Ширина', blank=True, max_length=20, help_text="Артикул")
    height = models.CharField('Высота', blank=True, max_length=20, help_text="Артикул")
    length_unit = models.CharField('Габарит', blank=True, max_length=20, help_text="Артикул")
    status = models.CharField('Наличие', blank=True, max_length=20, help_text="Артикул")
    tax_class_id = models.CharField('Налог', blank=True, max_length=20, help_text="Артикул")
    seo_keyword = models.CharField('Url ЧПУ', blank=True, max_length=20, help_text="Артикул")
    description = models.CharField('Описание', blank=True, max_length=20, help_text="Артикул")
    meta_title = models.CharField('title', blank=True, max_length=20, help_text="Артикул")
    meta_description = models.CharField('Снипет', blank=True, max_length=20, help_text="Артикул")
    meta_h1 = models.CharField('Заголовок H1', blank=True, max_length=20, help_text="Артикул")
    meta_keywords = models.CharField('Ключевые слова', blank=True, max_length=20, help_text="Артикул")
    stock_status_id = models.CharField('Наличие в продаже', blank=True, max_length=20, help_text="Артикул")
    store_ids = models.CharField('Магазин', blank=True, max_length=20, help_text="Артикул")
    layout = models.CharField('Сорт', blank=True, max_length=20, help_text="Артикул")
    related_ids = models.CharField('Аналоги', blank=True, max_length=20, help_text="Артикул")
    tags = models.CharField('Тэги', blank=True, max_length=20, help_text="Артикул")
    sort_order = models.CharField('Сортировка', blank=True, max_length=20, help_text="Артикул")
    subtract = models.CharField('Резервирование', blank=True, max_length=20, help_text="Артикул")
    minimum = models.CharField('Минимальный остаток', blank=True, max_length=20, help_text="Артикул")






class News(models.Model):
    article = models.CharField(max_length=20, help_text="Enter field documentation")
    text_news = models.TextField(max_length=20, help_text="Enter field documentation")
    data = models.DateTimeField(blank=True, verbose_name="Дата")


#
#
class OrderItem(models.Model):
    name = models.CharField('Заводчик', max_length=30, help_text="Фамилия и имя")
    # phone = models.CharField(max_length=10, help_text="Номер телефона")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField('Телефон', validators=[phoneNumberRegex], max_length=16, unique=True)
    article = models.CharField('Артикул', max_length=20, help_text="Артикул")
    message = models.TextField('Замечания', max_length=100, help_text="Замечания")
    order_data = models.DateTimeField(verbose_name="Дата")


#
#
class OrderItemTemporarity(models.Model):
    name = models.CharField('Волонтер', max_length=30, help_text="Фамилия и имя")
    # phone = models.CharField(max_length=10, help_text="Номер телефона")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField('Телефон', validators=[phoneNumberRegex], max_length=16, unique=True)
    article = models.CharField('Артикул', max_length=20, help_text="Артикул")
    order_data = models.DateTimeField(verbose_name="Дата")
    start_time = models.DateTimeField(verbose_name="Начало")
    end_time = models.DateTimeField(verbose_name="Окончание")
    message = models.TextField('Замечания', max_length=100, help_text="Замечания")
#
#
# class TransportationOrder(models.Model):
#     TRANSPORT_VAR = [
#
#      (1, 'Доставка еды, медикаментов и других небольших вещей'),
#      (2, 'Доставка сена или соломы, строительных материлов для будок и других крупногабаритных вещей'),
#      (3, 'Транспортировка небольших собак и котов'),
#      (4, 'Транспортировка больших собак')
#
#     ]
#     driver_name = models.CharField('Перевозчик', max_length=30, help_text="Инициалы")
#     # phone_numb = models.CharField(max_length=10, help_text="Телефон")
#     phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
#     phone = models.CharField('Телефон', validators=[phoneNumberRegex], max_length=16)
#     transport_type = models.IntegerField('Вид перевозки', null=True, choices=TRANSPORT_VAR)
#     order_data = models.DateTimeField(verbose_name="Дата")
#     start_point = models.CharField(max_length=30,verbose_name="Погрузить")
#     end_point = models.CharField(max_length=30,verbose_name="Выгрузить")
#     message = models.TextField('Замечания', max_length=100, help_text="Замечания")
#
#
# class VolOrder(models.Model):
#
#     VOL_VAR = [
#      (1, 'Хочу помогать на постоянной основе(расписание можно подобрать так, как будет вам удобно'),
#      (2, 'Готов помогать иногда.Хочу выбрать удобное для меня время')
#     ]
#     name_vol = models.CharField('Волонтер', max_length=30, help_text="Фамилия и имя")
#     # phone = models.CharField(max_length=10, help_text="Номер телефона")
#     phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
#     phone = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)
#     vol_type = models.IntegerField(null=True, verbose_name='vol_type', choices=VOL_VAR)
#     data_order = models.DateTimeField(verbose_name="Дата")
#     start_time = models.DateTimeField(verbose_name="Начало")
#     end_time = models.DateTimeField(verbose_name="Окончание")
#     message = models.CharField(max_length=100, help_text="Замечания")
#
# class MedicamentosAdd(models.Model):
#
#     MEDICAMENTOS_VAR = [
#         (1, 'цефтриаксон'),
#         (2, 'новокаин'),
#         (3, 'гискан'),
#         (4, 'гамавит'),
#         (5, 'катозал'),
#         (6, 'антитокс'),
#         (7, 'фоспренил'),
#         (8, 'энтеросгель'),
#         (9, 'препараты от глистов'),
#         (10, 'препараты от блох,клещей'),
#         (11, 'для заживления ран')
#     ]
#     med_type = models.IntegerField('Препарат', choices=MEDICAMENTOS_VAR)
#     med_weight = models.IntegerField()
#     name = models.CharField('Волонтер',max_length=30, help_text="Фамилия и имя")
#     phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
#     phone = models.CharField('Телефон', validators=[phoneNumberRegex], max_length=16, unique=True)
#
#
# class ForageAdd(models.Model):
#
#     FORAGE_VAR = [
#         (1, 'крупы'),
#         (2, 'Сухие корма'),
#         (3, 'Влажные корма'),
#         (4, 'Фарш для собак')
#
#     ]
#     forage_type = models.IntegerField(null=True, verbose_name='Вид корма', choices=FORAGE_VAR)
#     forage_weight = models.IntegerField()
#     name = models.CharField('Волонтер',max_length=30, help_text="Фамилия и имя")
#     phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
#     phone = models.CharField('Телефон', validators=[phoneNumberRegex], max_length=16, unique=True)
#
# class ItemAdd(models.Model):
#
#     ITEM_VAR = [
#         (1, 'Ошейники, поводки, намордники'),
#         (2, 'Опилки и солома'),
#         (3, 'Посуда'),
#         (4, 'Теплые вещи'),
#         (5, 'Будки')
#
#     ]
#     item_type = models.IntegerField(null=True, verbose_name='Категория', choices=ITEM_VAR)
#     item_qty = models.IntegerField()
#     which_item = models.CharField('Вещь', max_length=100, help_text="Замечания")
#     name = models.CharField('Волонтер',max_length=30, help_text="Фамилия и имя")
#     phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
#     phone = models.CharField('Телефон', validators=[phoneNumberRegex], max_length=16, unique=True)
