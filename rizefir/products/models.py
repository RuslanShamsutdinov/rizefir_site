# Create your models here.
from django.db import models


class Category(models.Model):
    category_name = models.TextField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    main_photo = models.ImageField(upload_to=f'img/categories/',
                                   height_field=None,
                                   width_field=None,
                                   max_length=100)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Цена',
                                max_digits=8,
                                decimal_places=2)
    description = models.TextField(max_length=100, blank=True)
    size = models.CharField(max_length=50, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        # db_table_comment = 'Продукция'
        ordering = ['category', 'size']
        indexes = [models.Index(fields=['category', 'size'])]


class Image(models.Model):
    title = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'img/products/',
                              height_field=None,
                              width_field=None,
                              max_length=100)
    main_photo = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
