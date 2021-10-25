from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Blog(models.Model):
    title = models.CharField(
        max_length=160,
        verbose_name='Заголовок',
        db_index=True)
    text = models.TextField(
        blank=True,
        verbose_name='Контент')
    image = models.ImageField(
        upload_to='image/%Y/%m/%d',
        verbose_name='Изображение')
    publish_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата Публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='Автор')
    is_published = models.BooleanField(
        default=True,
        verbose_name='Состаяние публикации')
    category = models.ForeignKey(
        "Category",
        on_delete=models.DO_NOTHING,
        verbose_name='Категория')
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(
        max_length=220,
        verbose_name='Категории')

    slug = models.SlugField(
        max_length=220,
        verbose_name= 'Url'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

class Contact(models.Model):
    first_name = models.CharField(max_length=60,verbose_name='Имя')
    last_name = models.CharField(max_length=200,verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Емайл')
    message = models.TextField(verbose_name='Сообщение')
    create_at = models.DateTimeField(auto_now=True,verbose_name='Дата создания')
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['-create_at']
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Sent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Отправить'
        verbose_name_plural = 'Отправить'
        ordering = ['-email']
    def __str__(self):
        return f"{self.first_name} {self.last_name}"