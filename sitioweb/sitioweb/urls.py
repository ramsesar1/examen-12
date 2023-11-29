# sitioweb/urls.py

from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myappsitio.urls')),  # Esta línea incluye las URLs de tu aplicación
    # ... otras URLs del proyecto ...
]
