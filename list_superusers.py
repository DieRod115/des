import os
import django

print("Configurando el entorno de Django...")

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'des.settings')  # Reemplaza 'mi_proyecto' con el nombre correcto
django.setup()

print("Entorno configurado. Importando el modelo User...")

from django.contrib.auth.models import User

print("Modelo User importado. Filtrando superusuarios...")

superusers = User.objects.filter(is_superuser=True)

if superusers.exists():
    print("Superusuarios encontrados:")
    for superuser in superusers:
        print(f'Username: {superuser.username}, Email: {superuser.email}')
else:
    print("No se encontraron superusuarios.")
