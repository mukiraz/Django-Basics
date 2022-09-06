from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=50)
    isActive = models.BooleanField(default  = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = True, related_name="products")
    slug = models.SlugField(default="", blank=True, null=False, db_index=True, unique=True)

    def __str__(self):
        return f"{self.name} {self.price}"


