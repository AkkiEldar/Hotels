from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone

from authentication_app.managers import MyAccountManager


class Account(AbstractUser):
    """ My user model """
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский')
    ]

    username_validator = UnicodeUsernameValidator()
    first_name_validator = UnicodeUsernameValidator()
    first_name = models.CharField(
        max_length=20,
        validators=[first_name_validator],
        verbose_name='Имя'

    )
    last_name = models.CharField(
        max_length=20,
        validators=[first_name_validator],
        verbose_name='Фамилия'
    )

    username = models.CharField(max_length=60,
                                unique=True,
                                validators=[username_validator],
                                error_messages={
                                    "unique": "A user with that username already exists."},
                                verbose_name='Никнейм')
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='avatar',
                                      null=True, blank=True,
                                      verbose_name='Аватар')
    gender = models.CharField(max_length=20,
                              choices=GENDER_CHOICES,
                              verbose_name='Пол',
                              blank=True, null=True)
    date_joined = models.DateField(verbose_name='Дата регистрации',
                                   default=timezone.now)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def str(self):
        return f'{self.username}'
