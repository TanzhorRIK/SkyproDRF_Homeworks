from django.db import models
from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    image = models.ImageField(verbose_name='изображение', **NULLABLE)
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    image = models.ImageField(upload_to='lesson/', verbose_name='изображение',
                              **NULLABLE)
    video_url = models.CharField(max_length=255, verbose_name="ссылка на видео",
                                 **NULLABLE)


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
