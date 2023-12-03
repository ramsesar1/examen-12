# insertar_alimentos.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sitioweb.settings")
django.setup()

from myappsitio.models import Alimento  # Ajusta esta línea según la ubicación real de tu modelo Alimento

def insertar_alimentos():
    alimentos = [
        {'nombre': 'Pan', 'cantidad': 500, 'medida': 'unidades'},
        {'nombre': 'Lata refresco', 'cantidad': 500, 'medida': 'unidades'},
        {'nombre': 'Mayonesa', 'cantidad': 500, 'medida': 'gr'},
        {'nombre': 'Mostaza', 'cantidad': 500, 'medida': 'gr'},
        {'nombre': 'Tomate', 'cantidad': 500, 'medida': 'gr'},
        {'nombre': 'Carne', 'cantidad': 500, 'medida': 'gr'},
        {'nombre': 'Papas', 'cantidad': 500, 'medida': 'gr'},
        {'nombre': 'Lechuga', 'cantidad': 500, 'medida': 'gr'},
        {'nombre': 'Queso cheddar', 'cantidad': 500, 'medida': 'unidades'},
        {'nombre': 'Cebolla', 'cantidad': 500, 'medida': 'gr'},
    ]

    for alimento_data in alimentos:
        Alimento.objects.create(**alimento_data)

if __name__ == "__main__":
    insertar_alimentos()
