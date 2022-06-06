from django.db import models
from simple_history.models import HistoricalRecords

class Product(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=255)
    description = models.TextField(verbose_name='Описание товара')
    manufacturer = models.ForeignKey("Manufacturer", verbose_name='Производитель', on_delete=models.CASCADE)
    category = models.ForeignKey("Category", verbose_name='Категория', on_delete=models.CASCADE)
    COLORS_CHOICES = (("WHITE", "Белый"), ("BLACK", "Чёрный"), ("RED", "Красный"))
    color = models.CharField(verbose_name='Цвет', choices=COLORS_CHOICES, default="WHITE", max_length=5)
    photo = models.ImageField(verbose_name='Фото', upload_to='img/products')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Manufacturer(models.Model):
    name = models.CharField(verbose_name='Наименование компании', max_length=255)
    description = models.TextField(verbose_name='Описание компании')
    country = models.CharField(verbose_name='Страна', max_length=255)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=255)
    description = models.TextField(verbose_name='Описание категории')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
