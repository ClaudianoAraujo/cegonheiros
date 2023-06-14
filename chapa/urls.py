from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin

from . import views

urlpatterns = [
    
    path("", views.base, name='base'),
    path('registro', views.register, name='registro'),
    path("detalhe/", views.detalhe, name='detalhe'),
    path("create/", views.create, name="create"),
    path("profile/<int:id>", views.profile, name="profile"),
    path("form1/", views.formes, name="form1"),
    path("form2/", views.create_chapa, name="form2"),
    path("login/", views.dologin, name="login"),
    path("formlogin/", views.formlogin, name="formlogin"),
    path("login2/", auth_views.LoginView.as_view(template_name='login.html'), name='login2'),
    path("buscar/", views.buscar, name="buscar"),
    path("buscar_chapa/", views.buscar_chapa, name="buscar_chapa"),
    
]