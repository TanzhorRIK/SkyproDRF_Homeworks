# Generated by Django 4.2.4 on 2023-09-17 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_remove_user_username_user_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='moderator',
            field=models.BooleanField(default=False, verbose_name='Модератор'),
        ),
    ]