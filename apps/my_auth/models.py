from django.core.validators import FileExtensionValidator
from django.db import models

from src.base.services import get_path_upload_avatar, validate_image_size


class AuthUser(models.Model):
    email = models.EmailField(max_length=120, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    display_name = models.CharField(max_length=30, blank=True, null=True )
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'webp']), validate_image_size]
    )

    @property
    def is_authenticated(self):
        return True
    '''Всегда возвращает True, это способ узнать, был ли пользователь аутентифицирован.
    '''

    def __str__(self):
        return self.email
