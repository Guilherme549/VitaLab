from django.urls import path
from . import views

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadasto"),
    path("login/", views.logar, name="login"),
]
