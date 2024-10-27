from django.urls import path
from . import views



urlpatterns = [
    path('novo_pet/', views.novo_pet, name="novo_pet"),
    path('seus_pets/', views.seus_pets, name="seus_pets"),
    path('remover_pet/<int:id>', views.remover_pet, name="remover_pet"),
<<<<<<< HEAD
=======
    path('ver_pet/<int:id>', views.ver_pet, name="ver_pet"),
>>>>>>> f2a86fb (page see pet, bug fix database)
]
