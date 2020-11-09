from django.conf.urls import url, include
from . import views



urlpatterns = [
    url(r'^$', views.MainView.as_view()),
    url(r'student$', views.student),
    url(r'uchitel$', views.uchitel),
    url(r'add_urok$', views.add_urok),
    url(r'form_prepare$', views.form_prepare),
    url(r'uprav$', views.uprav),
    url(r'register$', views.RegisterFormView.as_view()),
    url(r'login$', views.LoginFormView.as_view()),
    url(r'logout$', views.LogoutView.as_view()),

]