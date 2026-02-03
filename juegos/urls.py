from django import urls
from django.urls import path
from .views import juego_list, juego_create, juego_update, juego_delete


urlpatterns = [
    path('', juego_list.as_view(), name='juego_list'),
    path('crear/', juego_create.as_view(), name='juego_create'),
    path('actualizar/<int:pk>/', juego_update.as_view(), name='juego_update'),
    path('borrar/<int:pk>/', juego_delete.as_view(), name='juego_delete'),
]