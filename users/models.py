from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    klass = models.PositiveSmallIntegerField(default=0, verbose_name = 'Номер Класса')
    imya = models.TextField(max_length=50, default='-', verbose_name = 'Имя')
    familiya = models.TextField(max_length=50, default='-', verbose_name = 'Фамилия')
    otchestvo = models.TextField(max_length=50, default='-', verbose_name = 'Отчество')
    telefon = models.TextField(max_length=50, default='-', verbose_name = 'Телефон')
    grupa = models.TextField(max_length=50, default='-', verbose_name = 'Группа')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email