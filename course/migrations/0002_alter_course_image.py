# Generated by Django 4.2.4 on 2023-08-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='lesson/', verbose_name='изображение'),
        ),
    ]