from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import Usuario
from django.views.decorators.csrf import csrf_protect
#config usuario
# views.py



def config_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('name')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contra')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        # Verificar si el correo electrónico ya está en uso
        if Usuario.objects.filter(correo=correo).exists():
            messages.error(request, 'Este correo electrónico ya está registrado. Por favor, elige otro.')
            return render(request, 'myappsitio/configusuario.html')

        # Hash de la contraseña antes de guardarla en la base de datos
        contraseña_hasheada = make_password(contraseña)

        # Crear un nuevo usuario y guardarlo en la base de datos
        nuevo_usuario = Usuario(
            nombre=nombre,
            correo=correo,
            contraseña=contraseña_hasheada,
            telefono=telefono,
            direccion=direccion
        )
        nuevo_usuario.save()

        # Redirigir a la página de inicio o a donde desees
        return redirect('pagina_inicio')

    return render(request, 'myappsitio/configusuario.html')







