# Generated by Django 3.0.8 on 2021-11-23 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0006_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='subcategoria',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
