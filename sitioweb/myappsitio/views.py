from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import Usuario


#registro



def registrar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('name')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contra')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        # Verificar si el correo electrónico ya está en uso
        if Usuario.objects.filter(correo=correo).exists():
            messages.error(request, 'Este correo electrónico ya está registrado. Por favor, elige otro.')
            return render(request, 'myappsitio/registro.html')

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

    return render(request, 'myappsitio/registro.html')







#login

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.hashers import check_password  # Importa check_password
from .models import Usuario

def iniciar_sesion(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')

        if not correo or not contraseña:
            messages.error(request, 'Por favor, ingresa tu correo y contraseña.')
            return render(request, 'myappsitio/login.html')

        # Consultar la base de datos para autenticar al usuario
        usuario = Usuario.objects.filter(correo=correo).first()

        if usuario is not None and check_password(contraseña, usuario.contraseña):
            # Autenticación exitosa
            login(request, usuario)
            return redirect('inicio_view/')  # Redirigir a la página de inicio
        else:
            messages.error(request, 'Inicio de sesión fallido. Comprueba tu correo y contraseña.')
            return render(request, 'myappsitio/login.html')

    return render(request, 'myappsitio/login.html')




#inicio

# views.py
from django.shortcuts import render, redirect

# ... otras importaciones ...


def redireccionar_inicio(request):
    # Puedes realizar cualquier lógica adicional aquí antes de redirigir
    return redirect('inicio_view')

def inicio_view(request):
    return render(request, 'myappsitio/inicio.html')



#carrito 

# myappsitio/views.py

from django.shortcuts import render, redirect

# ... otras importaciones ...

def carrito_view(request):
    # Puedes realizar cualquier lógica adicional aquí antes de renderizar la página
    return render(request, 'myappsitio/carrito.html')


from django.shortcuts import render


#historial
def historial_view(request):
    # Puedes agregar lógica adicional aquí según sea necesario
    return render(request, 'myappsitio/historial.html')


#menu
def menu_view(request):
    # Puedes agregar lógica adicional aquí según sea necesario
    return render(request, 'myappsitio/menu.html')



#configuracionusuario
def configusuario_view(request):
    # Puedes agregar lógica adicional aquí según sea necesario
    return render(request, 'myappsitio/configusuario.html')
