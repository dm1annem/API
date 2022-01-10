from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=120, blank=True, verbose_name='Заголовок', default='')
    video_link = models.URLField(max_length=200, null=True, blank=True, verbose_name='Ссылка на видео', default='')
    img = models.ImageField(upload_to='reviews', null=True, blank=True, verbose_name='Фото', default='')
    text = models.TextField(null=True, blank=True, verbose_name='Текст отзыва', default='')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    comment = models.CharField(max_length=220, blank=True, verbose_name='Комментарий', default='')
    owner = models.ForeignKey('auth.User', related_name='rewiews', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'
        ordering = ['-published']
