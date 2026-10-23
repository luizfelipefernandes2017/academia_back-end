from django.urls import path

from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("turmas/", views.lista_turmas, name="lista_turmas"),
]