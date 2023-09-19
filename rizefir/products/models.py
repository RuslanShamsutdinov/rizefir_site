from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.TextField(max_length=50)
    main_photo = models.ImageField(upload_to=f'static/media/img/categories/', height_field=None, width_field=None,
                                   max_length=100)
    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=100)
    size = models.CharField(max_length=50)
    is_published = models.BooleanField(default=True)
    # def get_image_path(self, name):
    # path = ''.join(["pictures/", slugify(name)])
    #     return path
    main_photo = models.ImageField(upload_to=f'static/media/img/{category}/', height_field=None, width_field=None,
                                   max_length=100)
    
    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        db_table_comment = 'Продукция'
        ordering = ['category', 'size']
        indexes = [models.Index(fields=['category', 'size'])]
