from django.urls import path
from . import views

urlpatterns = [
path('', views.listar_pets, name="listar_pets"),
<<<<<<< HEAD
=======
path('pet/<int:id_pet>/', views.pedido_adocao, name="pedido_adocao"),
>>>>>>> f2a86fb (page see pet, bug fix database)
]
