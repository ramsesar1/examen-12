# myappsitio/urls.py

from django.urls import path
from .views import iniciar_sesion, registrar_usuario, redireccionar_inicio, inicio_view, carrito_view, historial_view, menu_view, configusuario_view

urlpatterns = [
    path('', iniciar_sesion, name='pagina_inicio'),
    path('registrar/', registrar_usuario, name='registrar_usuario'),
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('inicio_view/', inicio_view, name='inicio_view'),
    path('redireccionar_inicio/', redireccionar_inicio, name='redireccionar_inicio'),
    path('historial/', historial_view, name='historial_view'),
    path('menu/', menu_view, name='menu_view'),
    path('configusuario/', configusuario_view, name='configusuario_view'),
    path('carrito/', carrito_view, name='carrito_view'),
    # ... otras URLs de tu aplicación ...
]
