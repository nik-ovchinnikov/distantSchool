from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from users.models import CustomUser
from .models import NomeraKlassa
from .models import Predmety
from .models import Prepodavately
from .models import Uroki, NomeraUroka, NomeraKlassa, Predmety, Prepodavately



class UserCreateForm(UserCreationForm):

    klass_nomer = forms.IntegerField(required=True)

    class Meta:
        model = CustomUser
        fields = ( "password1", "password2", "klass", "email")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.klass_nomer = self.cleaned_data["klass_nomer"]
        if commit:

            user.save()
        return user

class UrokiForm(ModelForm):
    class Meta:
        model = Uroki
        fields = ['date_field', 'nomer_uroka', 'nomer_klassa', 'vremya_nachala_uroka', 'nazvanie_predmeta', 'prepodavatel', 'tema_uroka', 'ssylka_na_urok', 'kod_dostupa', 'kommentaryi']




