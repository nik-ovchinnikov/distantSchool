from django.contrib import admin
from . import models

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Prepodavately
# Register your models here.

admin.site.register(models.Uroki)
admin.site.register(models.NomeraUroka)
admin.site.register(models.NomeraKlassa)
admin.site.register(models.Predmety)
admin.site.register(models.Prepodavately)


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import Group
#
# from .forms import UserChangeForm
# from .forms import UserCreationForm
# from .models import ExtUser
#
#
# class UserAdmin(UserAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm
#
#     list_display = [
#         'email',
#         'firstname',
#         'is_admin',
#         'lastname',
#         'middlename',
#     ]
#
#     list_filter = ('is_admin',)
#
#     fieldsets = (
#                 (None, {'fields': ('email', 'password')}),
#                 ('Personal info', {
#                  'fields': (
#                      'avatar',
#                      'firstname',
#                      'lastname',
#                      'middlename',
#                  )}),
#                 ('Permissions', {'fields': ('is_admin',)}),
#                 ('Important dates', {'fields': ('last_login',)}),
#     )
#
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': (
#                 'email',
#                 'password1',
#                 'password2'
#             )}
#          ),
#     )
#
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()
#
# # Регистрация нашей модели
# admin.site.register(ExtUser, UserAdmin)
# admin.site.unregister(Group)

#====================================================
