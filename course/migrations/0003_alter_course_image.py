# Generated by Django 4.2.4 on 2023-08-28 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='изображение'),
        ),
    ]
