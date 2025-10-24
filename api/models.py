from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    img = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    ckeditor = RichTextUploadingField()  # CKEditor с загрузкой изображений

    class Meta:
        verbose_name = 'Наши услуги'
        verbose_name_plural = 'Наши услугии'

    def __str__(self):
        return self.title


class About(models.Model):
    img = models.ImageField(upload_to='about/', verbose_name='Фото')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание проекта')

    def __str__(self):
        return self.title

class Project(models.Model):
    img = models.ImageField(upload_to='projects/', verbose_name='Фото проекта')
    title = models.CharField(max_length=255, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание проекта')
    link = models.URLField(blank=True, null=True, verbose_name='Ссылка на проект')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Наши проекты'

    def __str__(self):
        return self.title

class Consultation(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    message = models.TextField(verbose_name='Что вас интересует')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'{self.name} ({self.phone})'

from django.db import models


# ⚙️ Инструменты / Технологии
class Tool(models.Model):
    img = models.ImageField(upload_to='tools/', verbose_name='Логотип')
    title = models.CharField(max_length=255, verbose_name='Название технологии')

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'

    def __str__(self):
        return self.title


from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя клиента')
    position = models.CharField(max_length=150, verbose_name='Должность / компания')
    text = models.TextField(verbose_name='Отзыв')
    photo = models.ImageField(upload_to='reviews/', verbose_name='Фото', blank=True, null=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.name} — {self.position}'
