from django.urls import path

from . import views

urlpatterns = [
    path("", views.base, name='base'),
    path('registro', views.register, name='registro'),
    path("detalhe/", views.detalhe, name='detalhe'),
    path("create/", views.create, name="create"),
    path("profile/<int:id>", views.profile, name="profile"),
    path("formes/", views.formes, name="formes"),
    path("create-chapa/", views.create_chapa, name="formes2"),
    path("login/", views.dologin, name="login"),
    path("formlogin/", views.formlogin, name="formlogin"),
]