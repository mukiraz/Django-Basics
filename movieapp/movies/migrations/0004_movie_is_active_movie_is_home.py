# Generated by Django 4.1.1 on 2022-09-07 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_options_alter_person_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
    ]