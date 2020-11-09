from django.db import models
from django.contrib.auth.models import User


from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models


# class UserManager(BaseUserManager):
#
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError('Email непременно должен быть указан')
#
#         user = self.model(
#             email=UserManager.normalize_email(email),
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password):
#         user = self.create_user(email, password)
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
#
#
# class ExtUser(AbstractBaseUser, PermissionsMixin):
#
#     email = models.EmailField(
#         'Электронная почта',
#         max_length=255,
#         unique=True,
#         db_index=True
#     )
#
#     firstname = models.CharField(
#         'Фамилия',
#         max_length=40,
#         null=True,
#         blank=True
#     )
#     lastname = models.CharField(
#         'Имя',
#         max_length=40,
#         null=True,
#         blank=True
#     )
#     middlename = models.CharField(
#         'Отчество',
#         max_length=40,
#         null=True,
#         blank=True
#     )
#
#     register_date = models.DateField(
#         'Дата регистрации',
#         auto_now_add=True
#     )
#     is_active = models.BooleanField(
#         'Активен',
#         default=True
#     )
#     is_admin = models.BooleanField(
#         'Суперпользователь',
#         default=False
#     )
#
#     # Этот метод обязательно должен быть определён
#     def get_full_name(self):
#         return self.email
#
#     # Требуется для админки
#     @property
#     def is_staff(self):
#         return self.is_admin
#
#     def get_short_name(self):
#         return self.email
#
#     def __str__(self):
#         return self.email
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = UserManager()
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'

# Create your models here.

class NomeraUroka(models.Model):
    nomer_uroka = models.PositiveSmallIntegerField()

    def __str__(self):
          return str(self.nomer_uroka)

    class Meta:
        verbose_name = 'Номер Урока'
        verbose_name_plural = 'Номера Уроков'

class NomeraKlassa(models.Model):
    nomer_klassa = models.PositiveSmallIntegerField()

    def __str__(self):
          return str(self.nomer_klassa)

    class Meta:
        verbose_name = 'Номер Класса'
        verbose_name_plural = 'Номера Классов'

class Predmety(models.Model):
    nazvanie_predmeta = models.TextField(max_length=25)

    def __str__(self):
         return self.nazvanie_predmeta

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

class Prepodavately(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.TextField(max_length=50, default='-')

    imya = models.TextField(max_length=50, default='-', verbose_name = 'Имя')
    otchestvo = models.TextField(max_length=50, default='-', verbose_name = 'Отчество')
    familiya = models.TextField(max_length=50, default='-', verbose_name = 'Фамилия')

    login = models.TextField(max_length=50, default='-')
    parol = models.TextField(max_length=50, default='-')
    email = models.TextField(max_length=50, default='-')
    telefon = models.TextField(max_length=50, default='-')

    def __str__(self):
         return self.imya + " " + self.otchestvo + " " + self.familiya

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Uroki(models.Model):
    date_field = models.DateField(verbose_name = 'Дата')
    nomer_uroka = models.ForeignKey(NomeraUroka, on_delete=models.CASCADE, verbose_name = 'Номер урока')
    vremya_nachala_uroka = models.CharField(max_length=5, verbose_name = 'Время начала урока')
    nomer_klassa = models.ForeignKey(NomeraKlassa, on_delete=models.CASCADE, verbose_name = 'Номер класса')
    nazvanie_predmeta = models.ForeignKey(Predmety, on_delete=models.CASCADE, verbose_name = 'Название предмета')
    prepodavatel = models.ForeignKey(Prepodavately, on_delete=models.CASCADE, verbose_name = 'Преподаватель')
    tema_uroka = models.CharField(max_length=500, verbose_name = 'Тема Урок')
    ssylka_na_urok = models.CharField(max_length=10000, default="-", verbose_name = 'Ссылка на урок')
    kommentaryi = models.TextField(max_length=10000, verbose_name = 'Комментарий')
    kod_dostupa = models.CharField(max_length=20, verbose_name = 'Код доступа')

    def __str__(self):
        return str(self.date_field) + "    " + str(self.nazvanie_predmeta) + " " + str(self.nomer_klassa)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'



class Upravlenie(models.Model):
    imya = models.TextField(max_length=50, default='-')
    otchestvo = models.TextField(max_length=50, default='-')
    familiya = models.TextField(max_length=50, default='-')
    login = models.TextField(max_length=50, default='-')
    parol = models.TextField(max_length=50, default='-')
    email = models.TextField(max_length=50, default='-')
    telefon = models.TextField(max_length=50, default='-')

    def __str__(self):
         return self.imya + " " + self.otchestvo + " " + self.familiya

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'








