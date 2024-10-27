from django.urls import path
from . import views

urlpatterns = [
path('', views.listar_pets, name="listar_pets"),

path('pet/<int:id_pet>/', views.pedido_adocao, name="pedido_adocao"),
]