from django.db import models
from django_extensions.db.fields import AutoSlugField


class Category(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Images(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    image = models.ImageField(upload_to='images', verbose_name="Изображение", null=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Brand(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.title


class Specification(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return self.title


class Association(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Ассоциация'
        verbose_name_plural = 'Ассоциации'

    def __str__(self):
        return self.title


class Product(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False, default=0.0)
    sale = models.DecimalField(max_digits=9, decimal_places=2, null=False, default=0.0)
    date_add = models.DateTimeField(auto_now_add=True)
    date_rewrite = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(max_length=50, unique=True, populate_from='title')

    category = models.ForeignKey(Category, verbose_name="Категория", null=True, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name="Бренд", null=True, on_delete=models.CASCADE)
    images = models.ManyToManyField(Images)
    info = models.ManyToManyField(Association)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title
# остальные классы для авторизации и оплаты и тд в других приложениях писать здесь толькр для товаров )