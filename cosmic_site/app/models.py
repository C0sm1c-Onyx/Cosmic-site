from django.db import models


class Facts(models.Model):
    title = models.CharField(max_length=999, verbose_name="Заголовок")
    text = models.TextField(max_length=3000, verbose_name="Текст")
    photo = models.ImageField(upload_to='photos/%Y/', verbose_name='Фото')
