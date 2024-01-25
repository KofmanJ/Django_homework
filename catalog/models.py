from django.conf import settings
from django.db import models

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Наименование продукта')
    product_description = models.TextField(max_length=100, verbose_name='Описание продукта')
    product_image = models.ImageField(upload_to='product_images', verbose_name='Изображение продукта', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Наименование категории')
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена продукта за единицу')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')  # Automatically set the date of
    date_last_modified = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения записи')  # Automatically set

    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='продавец')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product_name} - {self.product_description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        permissions = [
            (
                'set_published',
                'Can publish products'
            ),
        ]


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Наименование категории')
    category_description = models.TextField(max_length=100, verbose_name='Описание категории')

    def __str__(self):
        return f'{self.category_name} - {self.category_description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Version(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Наименование продукта')
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии')
    is_active = models.BooleanField(default=True, verbose_name='Активная версия')

    def __str__(self):
        return f'{self.product_name} - {self.version_number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
