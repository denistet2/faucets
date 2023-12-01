from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.core.validators import RegexValidator


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True, verbose_name='Оповещать о новинках?')

    class Meta(AbstractUser.Meta):
        pass

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']
    # order = models.SmallIntegerField(default=0, db_index=True, verbose_name='Порядок')
    # super_rubric = models.ForeignKey('SuperRubric', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Надрубрика')

# class SuperRubricManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(super_rubric__isnull=True)
#
# class SuperRubric(Categories):
#     objects = SuperRubricManager()
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         proxy = True
#         ordering = ('order', 'name')
#         verbose_name = 'Надрубрика'
#         verbose_name_plural = 'Надрубрики'
#
#
# class SubRubricManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(super_rubric__isnull=False)
#
# class SubRubric(Categories):
#     objects = SubRubricManager()
#     def __str__(self):
#         return '%s - %s' % (self.super_rubric.name, self.name)
#
#     class Meta:
#         proxy = True
#         ordering = ('super_rubric__order', 'super_rubric__name', 'order', 'name')
#         verbose_name = 'Подрубрика'
#         verbose_name_plural = 'Подрубрики'

# class Product(models.Model):
#     # Product_category = [
#     #
#     #     (1, 'Faucet'),
#     #     (2, 'Basin'),
#     #     (3, 'Accessory'),
#     #     (4, 'Gardeneqm'),
#     #     (5, 'Sewerage')
#     # ]
#     name = models.CharField('Наименование', blank=True, max_length=30, help_text="Артикул")
#
#     rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Категория')
#     # categories = models.ForeignKey('Categories', null=True, on_delete=models.PROTECT, choices=Product_category,help_text="Категория")
#     sku = models.CharField('Артикул', blank=True, max_length=20, help_text="Артикул")
#     upc = models.CharField('UPC', blank=False, max_length=20, help_text="Внутренний код")
#     ean = models.CharField('EAN', blank=True, max_length=20, help_text="Штрихкод")
#     jan = models.CharField('JAN', blank=True, max_length=20, help_text="Артикул")
#     isbn = models.CharField('ISBN', blank=True, max_length=20, help_text="Артикул")
#     mpn = models.CharField('MPN', blank=True, max_length=20, help_text="Артикул")
#     location = models.CharField('Размещение', blank=True, max_length=20, help_text="Артикул")
#     quantity = models.CharField('Количество', blank=True, max_length=20, help_text="Артикул")
#     model = models.CharField('Модель', blank=True, max_length=20, help_text="На упаковке")
#     manufacturer = models.CharField('Производитель', blank=True, max_length=20, help_text="Артикул")
#     image_name = models.CharField('Ссылка на фото', blank=True, max_length=20, help_text="ссылка")
#     foto = models.ImageField(upload_to='images', blank=True, verbose_name='Изображение')
#     shipping = models.CharField('Пересылка', blank=True, max_length=20, help_text="Артикул")
#     price = models.DecimalField('Цена', blank=True, help_text="Цена", max_digits=8, decimal_places=2)
#     points = models.CharField('Баллы', blank=True, max_length=20, help_text="Артикул")
#     date_added = models.DateTimeField('Дата добавления', auto_now_add=True, db_index=True)
#     date_modified = models.DateTimeField('Дата изменений', auto_now_add=True, db_index=True)
#     date_available = models.DateTimeField('Дата поступления', auto_now_add=True, db_index=True)
#     weight = models.CharField('Вес', blank=True, max_length=20, help_text="Артикул")
#     weight_unit = models.CharField('Вес нетто', blank=True, max_length=20, help_text="Артикул")
#     length = models.CharField('Длина', blank=True, max_length=20, help_text="Артикул")
#     width = models.CharField('Ширина', blank=True, max_length=20, help_text="Артикул")
#     height = models.CharField('Высота', blank=True, max_length=20, help_text="Артикул")
#     length_unit = models.CharField('Габарит', blank=True, max_length=20, help_text="Артикул")
#     status = models.CharField('Наличие', blank=True, max_length=20, help_text="Артикул")
#     tax_class_id = models.CharField('Налог', blank=True, max_length=20, help_text="Артикул")
#     seo_keyword = models.CharField('Url ЧПУ', blank=True, max_length=20, help_text="Артикул")
#     description = models.CharField('Описание', blank=True, max_length=20, help_text="Артикул")
#     meta_title = models.CharField('title', blank=True, max_length=20, help_text="Артикул")
#     meta_description = models.CharField('Снипет', blank=True, max_length=20, help_text="Артикул")
#     meta_h1 = models.CharField('Заголовок H1', blank=True, max_length=20, help_text="Артикул")
#     meta_keywords = models.CharField('Ключевые слова', blank=True, max_length=20, help_text="Артикул")
#     stock_status_id = models.CharField('Наличие в продаже', blank=True, max_length=20, help_text="Артикул")
#     store_ids = models.CharField('Магазин', blank=True, max_length=20, help_text="Артикул")
#     layout = models.CharField('Сорт', blank=True, max_length=20, help_text="Артикул")
#     related_ids = models.CharField('Аналоги', blank=True, max_length=20, help_text="Артикул")
#     tags = models.CharField('Тэги', blank=True, max_length=20, help_text="Артикул")
#     sort_order = models.CharField('Сортировка', blank=True, max_length=20, help_text="Артикул")
#     subtract = models.CharField('Резервирование', blank=True, max_length=20, help_text="Артикул")
#     minimum = models.CharField('Минимальный остаток', blank=True, max_length=20, help_text="Артикул")
#
#     class Meta:
#         verbose_name = 'Товар'
#         verbose_name_plural = 'Товары'
#
#
#

# class News(models.Model):
#     article = models.CharField(max_length=20, help_text="Enter field documentation")
#     text_news = models.TextField(max_length=20, help_text="Enter field documentation")
#     data = models.DateTimeField(blank=True, verbose_name="Дата")


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
class Favorites(models.Model):
    name = models.CharField('Волонтер', max_length=30, help_text="Фамилия и имя")
    # phone = models.CharField(max_length=10, help_text="Номер телефона")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField('Телефон', validators=[phoneNumberRegex], max_length=16, unique=True)
    article = models.CharField('Артикул', max_length=20, help_text="Артикул")
    order_data = models.DateTimeField(verbose_name="Дата")
    start_time = models.DateTimeField(verbose_name="Начало")
    end_time = models.DateTimeField(verbose_name="Окончание")
    message = models.TextField('Замечания', max_length=100, help_text="Замечания")
