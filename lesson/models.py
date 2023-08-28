from django.db import models

from users.models import NULLABLE


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