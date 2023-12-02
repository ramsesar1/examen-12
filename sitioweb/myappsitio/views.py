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

# views.py - iniciar_sesion
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import Usuario

def iniciar_sesion(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')

        if not correo or not contraseña:
            messages.error(request, 'Por favor, ingresa tu correo y contraseña.')
            return render(request, 'myappsitio/login.html')

        usuario = Usuario.objects.filter(correo=correo).first()

        if usuario is not None and check_password(contraseña, usuario.contraseña):
            # Autenticación exitosa
            login(request, usuario)

            # Almacena el correo electrónico en la variable de sesión
            request.session['last_logged_in_user'] = usuario.correo

            print(f"Iniciando sesión para el usuario: {usuario}")  # Agrega este print

            return redirect('inicio_view')  # Redirige al nombre de la vista en lugar de la URL directa
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



# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Historial  # Asegúrate de importar el modelo correcto

@csrf_exempt
def guardar_orden(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_items = data.get('selectedItems', {})
        
        # Obtener el usuario actualmente autenticado (asegúrate de que tu backend maneje la autenticación)
        usuario = request.user

        # Guardar la orden en el historial
        historial = Historial(usuario=usuario, detalles=json.dumps(selected_items))
        historial.save()

        return JsonResponse({'message': 'Orden guardada exitosamente'})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)



#historial

# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def historial_view(request):
    # Recupera el correo electrónico almacenado en la variable de sesión
    last_logged_in_user_email = request.session.get('last_logged_in_user')

    # Obtén el usuario correspondiente al correo electrónico
    last_logged_in_user = Usuario.objects.filter(correo=last_logged_in_user_email).first()

    # Puedes realizar otras operaciones con last_logged_in_user según sea necesario

    return render(request, 'myappsitio/historial.html', {'usuario': last_logged_in_user})


























#menu
def menu_view(request):
    # Puedes agregar lógica adicional aquí según sea necesario
    return render(request, 'myappsitio/menu.html')



#configuracionusuario
def configusuario_view(request):
    # Puedes agregar lógica adicional aquí según sea necesario
    return render(request, 'myappsitio/configusuario.html')
