# Generated by Django 5.0b1 on 2023-11-04 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basins_type', models.IntegerField(choices=[(1, 'Стальная'), (2, 'Иск.камень')], help_text='Вид товара', verbose_name='Назначение')),
                ('foto', models.ImageField(blank=True, upload_to='images', verbose_name='Фото')),
                ('article', models.CharField(help_text='Артикул', max_length=20, verbose_name='Артикул')),
                ('price', models.IntegerField(help_text='Цена', verbose_name='Цена')),
                ('text_about_item', models.TextField(help_text='О товаре', max_length=200, verbose_name='Краткое описание')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faucets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faucets_type', models.IntegerField(choices=[(1, 'Ванна'), (2, 'Мойки'), (3, 'Умывальник'), (4, 'Душ')], help_text='Вид товара', verbose_name='Назначение')),
                ('foto', models.ImageField(blank=True, upload_to='images', verbose_name='Фото')),
                ('article', models.CharField(help_text='Артикул', max_length=20, verbose_name='Артикул')),
                ('price', models.IntegerField(help_text='Цена', verbose_name='Цена')),
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
    ]
