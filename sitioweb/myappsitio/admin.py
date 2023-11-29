from django.contrib import admin
from django.urls import path
from .views import Usuario

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Register your models here. 
admin.site.register(Usuario)