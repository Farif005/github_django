from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Жанры'
        verbose_name = 'Жанр'
        ordering = ['title']


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='image/', verbose_name='Фото')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    genre = models.ForeignKey('Genre', null=True, on_delete=models.PROTECT, verbose_name='Жанр')

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
        ordering = ['-published']