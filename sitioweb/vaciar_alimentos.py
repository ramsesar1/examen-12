# vaciar_alimentos.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sitioweb.settings")
django.setup()

from myappsitio.models import Alimento

def vaciar_alimentos():
    Alimento.objects.all().delete()

if __name__ == "__main__":
    vaciar_alimentos()
