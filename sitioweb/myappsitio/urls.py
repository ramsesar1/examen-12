# myappsitio/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views, viewsconfig

urlpatterns = [
    path('', views.iniciar_sesion, name='pagina_inicio'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('config_usuario/', viewsconfig.config_usuario, name='config_usuario'),


    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('inicio_view/', views.inicio_view, name='inicio_view'),
    path('redireccionar_inicio/', views.redireccionar_inicio, name='redireccionar_inicio'),
    path('menu/', views.menu_view, name='menu_view'),
    path('carrito/', views.carrito_view, name='carrito_view'),
    path('guardar_orden/', views.guardar_orden, name='guardar_orden'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/login/', LoginView.as_view(template_name='myappsitio/login.html'), name='login'),
    path('historial/', views.historial_view, name='historial_view'),
    # ... otras URLs de tu aplicación ...
]
