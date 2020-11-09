from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from users.forms import CustomUserCreationForm
from . import forms

from .forms import UserCreateForm, UrokiForm
from .models import Uroki, Prepodavately
from datetime import datetime, timedelta


from .forms import UserCreateForm

# Create your views here.
# def start(request):
#     context = {
#         "greeting": "Здравствуй, гость",
#     }
#     return render(request, "start.html", context)

def student(request):
    klass = request.user.klass
    imya = request.user.imya
    all_lessons = Uroki.objects.filter(nomer_klassa=klass).order_by('-date_field', 'nomer_uroka')[:10]

    context = {
        "greeting": "Здравствуй, ученик",
        "imya": "Василий Сергеев",
        "nomerKlassa": klass,
        "uroki": all_lessons,
        "imya": imya,
    }
    return render(request, "student.html", context)

def uchitel(request):

    #Получение вчерашней даты
    today = datetime.now()
    yesterday = today - timedelta(days=1)

    #Forma
    form_for_new_urok = forms.UrokiForm

    #Filter Prepod
    prepod_name = request.user.imya
    print(prepod_name)
    prepod_otch = request.user.otchestvo
    prepod_id = prepod_name + " " + prepod_otch
    prepod_id2 = Prepodavately.objects.get(imya=prepod_name, otchestvo=prepod_otch)
    all_lessons = Uroki.objects.filter(prepodavatel=prepod_id2).order_by('-date_field', 'nomer_uroka')[:30]
    #all_lessons = all_lessons.filter(date_field=today)

    #all_lessons = Uroki.objects.order_by('-date_field', 'nomer_uroka')[:10]

    context = {
        'uchitel_name': prepod_id,
        'greeting': "Здравствуйте, ",
        'urokForm': form_for_new_urok,
        'IO': prepod_name,

        "uroki": all_lessons
    }
    return render(request, "uchitel.html", context)

def form_prepare(request):

    # Запрос на данные по запросу id
    if request.POST['needFormNomer']:
        formToUpdate = Uroki.objects.get(id=request.POST['needFormNomer'])
        formToUpdate = formToUpdate.__dict__
        # print(formToUpdate)
        data = {
            "date_field": formToUpdate['date_field'],
            "id": formToUpdate['id'],
            "nomer_uroka_id": formToUpdate['nomer_uroka_id'],
            "vremya_nachala_uroka": formToUpdate['vremya_nachala_uroka'],
            "nomer_klassa_id": formToUpdate['nomer_klassa_id'],
            "nazvanie_predmeta_id": formToUpdate['nazvanie_predmeta_id'],
            "prepodavatel_id": formToUpdate['prepodavatel_id'],
            "tema_uroka": formToUpdate['tema_uroka'],
            "ssylka_na_urok": formToUpdate['ssylka_na_urok'],
            "kommentaryi": formToUpdate['kommentaryi'],
            "kod_dostupa": formToUpdate['kod_dostupa'],
        }
        return JsonResponse(data)

def add_urok(request):

        print(request.POST)
        if request.POST:

            if request.POST['ID'] == '':
                #На добавление
                print("Form wothout ID")
                form = UrokiForm(request.POST)
                if form.is_valid():
                    form.save()
                    return render(request, "add_urok.html")



            else:
                #На исправление
                print(request.POST['ID'])

                urokForm = UrokiForm(request.POST)
                if urokForm.is_valid():
                    urok = Uroki.objects.get(id=request.POST['ID'])
                    urokForm = UrokiForm(request.POST, instance = urok)
                    urokForm.save()
                    return render(request, "add_urok.html")



            # result = "Урок успешно добавлен %s" %request.path
            # if request.method == 'POST':
            #     if form.is_valid():
            #         data = form.cleaned_data
            #         #form.save()
            #         print(data['nazvanie_predmeta'])
            #
            #         return render(request, "add_urok.html")


def uprav(request):

    all_lessons = Uroki.objects.order_by('-date_field', 'nomer_uroka')[:20]

    context = {
        'uprav_name': "Василий Васильевич",
        'greeting': "Здравствуйте, ",

        "uroki": all_lessons
    }
    return render(request, "uprav.html", context)

class MainView(TemplateView):
    template_name = 'start.html'

    def get(self, request):
        if request.user.is_authenticated:
            if request.user.grupa == "ученик":
                print("2Heloo2!")
                #uchitel(request)
            #return render(request, self.template_name, ctx)

                return HttpResponseRedirect("/shkola/student")

            elif request.user.grupa == "учитель":
                print("332Heloo3!")
                return HttpResponseRedirect("/shkola/uchitel")

            elif request.user.grupa == "управление":
                print("332Heloo3!")
                return HttpResponseRedirect("/shkola/uprav")
            else:
                #student(request)
                print("Heloo2!")
                return render(request, "uchitel.html", {})
        else:
            return render(request, self.template_name, {})

class RegisterFormView(FormView):
    form_class = CustomUserCreationForm
    success_url = "login"

    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):

        return super(RegisterFormView, self).form_invalid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "/shkola/"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/shkola")