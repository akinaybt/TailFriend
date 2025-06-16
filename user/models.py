from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_vetworker = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True
    )

    GENDER = (
        ('Male', "Мужчина"),
        ('Female', 'Женщина'),
        ('NotSpecified', 'Не указывать')
    )

    gender = models.CharField(max_length=15, choices=GENDER, default='NotSpecified')

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return f"Профиль пользователя {self.user}"

class VetClinicUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ветеринар'
        verbose_name_plural = 'Ветеринары'

    def __str__(self):
        return f'{self.user}'


