from pickle import TRUE
from tkinter import CASCADE
from turtle import mode
from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contact(models.Model):
    address = models.CharField(max_length=200)
    email = models.EmailField(null = True)

    def __str__(self):
        return self.address

class Person(models.Model):
    genders = (
        ('M','Erkek'),
        ('F','Kadın')
    )

    duty_types = (
        ('1', 'Görevci'),
        ('2', 'Oyuncu'),
        ('3', 'Yönetmen'),
        ('4', 'Senarist'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.CharField(max_length=3000)
    image_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=genders)
    duty_type = models.CharField(max_length=1, choices=duty_types)
    contact = models.OneToOneField(Contact, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.duty_types[int(self.duty_type) - 1][1]})"

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(validators=[MinLengthValidator(20)])
    image_name = models.CharField(max_length=50)
    image_cover = models.CharField(max_length=50)
    date = models.DateField()
    slug = models.SlugField(unique=TRUE, db_index = True)
    budget = models.DecimalField(max_digits=19, decimal_places=2)
    language = models.CharField(max_length=100)
    people = models.ManyToManyField(Person)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
