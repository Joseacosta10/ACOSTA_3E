from django.urls import path
from . import views

urlpatterns = [
    path('', views.holamundoCore,name='core'),
    path('noticias1',views.noticias,name='noticias'),
    path('deportes1',views.deportes,name='deportes'),


    path('inicio',views.inicio,name='inicio'),
    path('quienes_somos',views.quienes_somos,name='quienes_somos'),
    path('nuestro_producto',views.nuestro_producto,name='nuestro_producto'),
    path('contacto', views.contacto, name='contacto'),
    path('quienes_somos2', views.quienes_somos2, name='quienes_somos2'),
]




