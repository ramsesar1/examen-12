from django.contrib import admin
from django.urls import path
from .views import Usuario
from .models import Alimento
from .models import Historial

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Register your models here. 
admin.site.register(Usuario)
admin.site.register(Alimento)
admin.site.register(Historial)