# Generated by Django 5.0b1 on 2023-11-09 19:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_type', models.IntegerField(choices=[(1, 'Стальная'), (2, 'Иск.камень')], help_text='Вид товара', verbose_name='Назначение')),
                ('foto', models.ImageField(blank=True, upload_to='images', verbose_name='Фото')),
                ('article', models.CharField(help_text='Артикул', max_length=20, verbose_name='Артикул')),
                ('price', models.DecimalField(decimal_places=2, help_text='Цена', max_digits=4, verbose_name='Цена')),
                ('text_about_item', models.TextField(help_text='О товаре', max_length=200, verbose_name='Краткое описание')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Basins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basins_type', models.IntegerField(choices=[(1, 'Стальная'), (2, 'Иск.камень')], help_text='Вид товара', verbose_name='Назначение')),
                ('foto', models.ImageField(blank=True, upload_to='images', verbose_name='Фото')),
                ('article', models.CharField(help_text='Артикул', max_length=20, verbose_name='Артикул')),
                ('price', models.DecimalField(decimal_places=2, help_text='Цена', max_digits=4, verbose_name='Цена')),
                ('text_about_item', models.TextField(help_text='О товаре', max_length=200, verbose_name='Краткое описание')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gardeneqm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_type', models.IntegerField(choices=[(1, 'Ерш'), (2, 'Полка')], help_text='Вид товара', verbose_name='Назначение')),
                ('foto', models.ImageField(blank=True, upload_to='images', verbose_name='Фото')),
                ('article', models.CharField(help_text='Артикул', max_length=20, verbose_name='Артикул')),
                ('price', models.DecimalField(decimal_places=2, help_text='Цена', max_digits=4, verbose_name='Цена')),
                ('text_about_item', models.TextField(help_text='О товаре', max_length=200, verbose_name='Краткое описание')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(help_text='Enter field documentation', max_length=20)),
                ('text_news', models.TextField(help_text='Enter field documentation', max_length=20)),
                ('data', models.DateTimeField(blank=True, verbose_name='Дата')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Фамилия и имя', max_length=30, verbose_name='Заводчик')),
                ('phone', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Телефон')),
                ('article', models.CharField(help_text='Артикул', max_length=20, verbose_name='Артикул')),
                ('message', models.TextField(help_text='Замечания', max_length=100, verbose_name='Замечания')),
                ('order_data', models.DateTimeField(verbose_name='Дата')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItemTemporarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Фамилия и имя', max_length=30, verbose_name='Волонтер')),
                ('phone', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Телефон')),
                ('article', models.CharField(help_text='Артикул', max_length=20, verbose_name='Артикул')),
                ('order_data', models.DateTimeField(verbose_name='Дата')),
                ('start_time', models.DateTimeField(verbose_name='Начало')),
                ('end_time', models.DateTimeField(verbose_name='Окончание')),
                ('message', models.TextField(help_text='Замечания', max_length=100, verbose_name='Замечания')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
                ('product_id', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Наименование')),
                ('categories', models.CharField(blank=True, choices=[(1, 'Смеситель'), (2, 'Мойки'), (3, 'Аксессуары'), (4, 'Канализация'), (5, 'Садовый полив')], help_text='Артикул', max_length=20, verbose_name='Категория')),
                ('sku', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Артикул')),
                ('upc', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='UPC')),
                ('ean', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='EAN')),
                ('jan', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='JAN')),
                ('isbn', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='ISBN')),
                ('mpn', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='MPN')),
                ('location', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Размещение')),
                ('quantity', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Количество')),
                ('model', models.CharField(blank=True, help_text='На упаковке', max_length=20, verbose_name='Модель')),
                ('manufacturer', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Производитель')),
                ('image_name', models.CharField(blank=True, help_text='фото', max_length=20, verbose_name='Изображение')),
                ('foto', models.ImageField(blank=True, upload_to='images', verbose_name='Фото')),
                ('shipping', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Пересылка')),
                ('price', models.DecimalField(blank=True, decimal_places=2, help_text='Цена', max_digits=8, verbose_name='Цена')),
                ('points', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Баллы')),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавления')),
                ('date_modified', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата изменений')),
                ('date_available', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата поступления')),
                ('weight', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Вес')),
                ('weight_unit', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Вес нетто')),
                ('length', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Длина')),
                ('width', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Ширина')),
                ('height', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Высота')),
                ('length_unit', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Габарит')),
                ('status', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Наличие')),
                ('tax_class_id', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Налог')),
                ('seo_keyword', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Url ЧПУ')),
                ('description', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Описание')),
                ('meta_title', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='title')),
                ('meta_description', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Снипет')),
                ('meta_h1', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Заголовок H1')),
                ('meta_keywords', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Ключевые слова')),
                ('stock_status_id', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Наличие в продаже')),
                ('store_ids', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Магазин')),
                ('layout', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Сорт')),
                ('related_ids', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Аналоги')),
                ('tags', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Тэги')),
                ('sort_order', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Сортировка')),
                ('subtract', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Резервирование')),
                ('minimum', models.CharField(blank=True, help_text='Артикул', max_length=20, verbose_name='Минимальный остаток')),
            ],
        ),
    ]
