from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """построение пути к файлу аватара, формат: (media)/avatar/user_id/foto.jpg
    """
    return f'avatar/{instance.id}/{file}'


def validate_image_size(file_obj):
    '''
    проверяем размер файла фото для аватара
    '''
    validate_size_image = 2
    if file_obj.size > validate_size_image * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла {validate_size_image}MB")