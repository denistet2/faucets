from django.db import models

# Create your models here.

class home_pet(models.Model):
    pets = models.CharField(max_length=20, help_text="Enter field documentation")
    name_pets = models.CharField(max_length=20, help_text="Enter field documentation")
    age_pets = models.CharField(max_length=20, help_text="Enter field documentation")
    text_about_pets = models.CharField(max_length=200, help_text="Enter field documentation")

class help_list(models.Model):
    help_id = models.CharField(max_length=20, help_text="Enter field documentation")


class order_help(models.Model):
    name = models.CharField(max_length=20, help_text="Имя")
    help_type = models.CharField(max_length=10)
    mail_adress = models.EmailField(max_length=10)
    phone_number = models.CharField(max_length=10)


class news(models.Model):
    pets = models.CharField(max_length=20, help_text="Enter field documentation")
    text_news = models.CharField(max_length=20, help_text="Enter field documentation")


class order_pet(models.Model):
    template_help = models.CharField(max_length=20, help_text="Enter field documentation")
