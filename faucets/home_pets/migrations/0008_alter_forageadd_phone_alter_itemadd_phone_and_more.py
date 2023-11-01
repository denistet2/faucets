# Generated by Django 4.1.5 on 2023-01-17 21:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_pets', '0007_forageadd_itemadd_medicamentosadd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forageadd',
            name='phone',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='itemadd',
            name='phone',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='medicamentosadd',
            name='phone',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='orderpettemporarity',
            name='phone',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Телефон'),
        ),
    ]