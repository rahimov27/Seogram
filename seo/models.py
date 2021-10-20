from django.db import models
from django.contrib.auth.models import User

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
        verbose_name='Состаяние Публикации')
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

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-title']

    def __str__(self):
        return self.title