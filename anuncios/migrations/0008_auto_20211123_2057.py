# Generated by Django 3.0.8 on 2021-11-23 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0007_auto_20211123_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(null=True, upload_to='img/%y'),
        ),
    ]
