from django.contrib.auth.models import AbstractUser
from django.db import models
import phonenumbers
from phonenumber_field.modelfields import PhoneNumberField
from TailFriend import settings

class CustomUser(AbstractUser):
  phone_number = PhoneNumberField(unique=True)

class UserProfile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile',
                              primary_key=True)

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



