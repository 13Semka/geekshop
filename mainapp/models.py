from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название', unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return f'{self.pk}. {self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('pk', )



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=128, verbose_name='Название', unique=True)
    image = models.ImageField(upload_to='product', blank=True, verbose_name='Изображение')
    short_desc = models.CharField(max_length=128, verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return f'{self.name} ({self.category.name})'


    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

