# Generated by Django 3.0.8 on 2021-11-23 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0008_auto_20211123_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(upload_to='img/anuncios/%y'),
        ),
    ]
