from django.db import models


class Products(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField
    price = models.IntegerField
    sale = models.IntegerField
    date_add = models.DateTimeField
    date_rewrite = models.DateTimeField
    slug = models.SlugField

    # category =
    # brand =
    # images =
    # info =


class Category(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    title = models.CharField(max_length=255)


class Images(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    title = models.CharField(max_length=255)


class Brands(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    title = models.CharField(max_length=255)


class Info(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    title = models.CharField(max_length=255)


class Associations(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, unique=True)
    title = models.CharField(max_length=255)

# остальные классы для авторизации и оплаты и тд в других приложениях писать здесь толькр для товаров )