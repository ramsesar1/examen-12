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

        contraseña_hasheada = make_password(contraseña)

        nuevo_usuario = Usuario(
            nombre=nombre,
            correo=correo,
            contraseña=contraseña_hasheada,
            telefono=telefono,
            direccion=direccion
        )
        nuevo_usuario.save()

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

            request.session['last_logged_in_user'] = usuario.correo

            print(f"Iniciando sesión para el usuario: {usuario}")  

            return redirect('inicio_view') 
        else:
            messages.error(request, 'Inicio de sesión fallido. Comprueba tu correo y contraseña.')
            return render(request, 'myappsitio/login.html')

    return render(request, 'myappsitio/login.html')






#inicio

# views.py
from django.shortcuts import render, redirect



def redireccionar_inicio(request):
    return redirect('inicio_view')

def inicio_view(request):
    return render(request, 'myappsitio/inicio.html')



#carrito 


from django.shortcuts import render, redirect


def carrito_view(request):

    return render(request, 'myappsitio/carrito.html')





# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Historial  
from django.db import transaction
from .models import Alimento

@csrf_exempt
@transaction.atomic

def guardar_orden(request):
    if request.method == 'POST':
        try:
            estructura_consumo = {
                'REFRESCO': {'Lata refresco': 1},
                'PAPAS FRITAS': {'Papas': 2},
                'PACK INDIVIDUAL': {'Lata refresco': 1, 'Papas': 2, 'Panes': 2, 'Carne': 1, 'Tomate': 1, 'Lechuga': 1, 'Mostaza': 1, 'Mayonesa': 1},
                'PRIME': {'Panes': 2, 'Carne': 2, 'Tomate': 1, 'Lechuga': 1, 'Mostaza': 1, 'Mayonesa': 1},
                'GUACA-BACON': {'Panes': 2, 'Carne': 1, 'Tomate': 1, 'Lechuga': 1, 'Mostaza': 1, 'Mayonesa': 1},
                'LOW-CARB': {'Lechuga': 4, 'Carne': 1, 'Tomate': 1, 'Mostaza': 1, 'Mayonesa': 1},
                'PACK-4-FAMILY': {'Panes': 8, 'Carne': 4, 'Tomate': 4, 'Mostaza': 4, 'Mayonesa': 4},
            }

            # Obtener los datos JSON de la solicitud
            data = json.loads(request.body)
            
            # Obtener los detalles del carrito desde los datos JSON
            detalles = data.get('detalles', {})

            historial = Historial.objects.create(detalles=detalles)

            for producto, cantidad_consumida in detalles.items():
                if producto in estructura_consumo:
                    ingredientes = estructura_consumo[producto]

                    for ingrediente, cantidad in ingredientes.items():
                        try:
                            alimento_obj = Alimento.objects.get(nombre__iexact=ingrediente.strip())
                            alimento_obj.cantidad -= cantidad * cantidad_consumida
                            alimento_obj.save()
                        except Alimento.DoesNotExist:
                            return JsonResponse({'error': f'Alimento no encontrado: {ingrediente}'}, status=404)

            return JsonResponse({'mensaje': f'Orden guardada con éxito. ID: {historial.id}'})
        except json.JSONDecodeError as e:
            return JsonResponse({'error': f'Error al decodificar JSON: {str(e)}'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)





#historial

# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def historial_view(request):
    historial = Historial.objects.all()

    # Recupera el usuario que hizo login
    last_logged_in_user_email = request.session.get('last_logged_in_user')
    last_logged_in_user = Usuario.objects.filter(correo=last_logged_in_user_email).first()


    # Pasa tanto el historial como el usuario a la plantilla
    return render(request, 'myappsitio/historial.html', {'historial': historial, 'usuario': last_logged_in_user})




from django.shortcuts import render
from .models import Historial

def historial_compras_view(request):
    historial_compras = Historial.objects.all()

    return render(request, 'myappsitio/historial_compras.html', {'historial': historial_compras})























#menu
def menu_view(request):
    return render(request, 'myappsitio/menu.html')



#configuracionusuario
def configusuario_view(request):
    return render(request, 'myappsitio/configusuario.html')

#transaccioncompleta
def transaccioncompleta_view(request):
    return render (request, 'myappsitio/transaccioncompleta.html')