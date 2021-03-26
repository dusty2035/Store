from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=30, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    main_pic = models.ImageField(upload_to='images/')
    pic_1 = models.ImageField(upload_to='images/', blank=True)
    pic_2 = models.ImageField(upload_to='images/', blank=True)
    pic_3 = models.ImageField(upload_to='images/', blank=True)
    pic_4 = models.ImageField(upload_to='images/', blank=True)
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()