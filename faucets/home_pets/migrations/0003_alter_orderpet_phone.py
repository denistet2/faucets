# Generated by Django 4.1.5 on 2023-01-16 17:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_pets', '0002_rename_end_tame_orderpettemporarity_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderpet',
            name='phone',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]