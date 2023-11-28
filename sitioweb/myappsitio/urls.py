# myappsitio/urls.py

from django.urls import path
from .views import iniciar_sesion, registrar_usuario, redireccionar_inicio, inicio_view
#inicio_view

urlpatterns = [
    path('', iniciar_sesion, name='pagina_inicio'),
    path('registrar/', registrar_usuario, name='registrar_usuario'),
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('inicio_view/', inicio_view, name='inicio_view'),
        path('redireccionar_inicio/', redireccionar_inicio, name='redireccionar_inicio'),  # Nueva URL

    # ... otras URLs de tu aplicación ...
]
