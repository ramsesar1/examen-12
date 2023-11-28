from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Usuario


#registro usuario

def registrar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('name')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contra')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        # Crear un nuevo usuario y guardarlo en la base de datos
        nuevo_usuario = Usuario(nombre=nombre, correo=correo, contraseña=contraseña, telefono=telefono, direccion=direccion)
        nuevo_usuario.save()

        # Redirigir a la página de inicio o a donde desees
        return redirect('pagina_inicio')


    return render(request, 'myappsitio/registro.html')



#login

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Usuario

def iniciar_sesion(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')

        if not correo or not contraseña:
            messages.error(request, 'Por favor, ingresa tu correo y contraseña.')
            return render(request, 'myappsitio/login.html')

        # Consultar la base de datos para autenticar al usuario
        usuario = authenticate(request, correo=correo, contraseña=contraseña)

        if usuario is not None:
            login(request, usuario)
            return redirect('inicio_view/')  # Redirigir a la página de inicio
        else:
            messages.error(request, 'Inicio de sesión fallido. Comprueba tu correo y contraseña.')
            return render(request, 'myappsitio/login.html')

    return render(request, 'myappsitio/login.html')



# views.py
from django.shortcuts import render, redirect

# ... otras importaciones ...

def redireccionar_inicio(request):
    # Puedes realizar cualquier lógica adicional aquí antes de redirigir
    return redirect('inicio_view')

def inicio_view(request):
    return render(request, 'myappsitio/inicio.html')