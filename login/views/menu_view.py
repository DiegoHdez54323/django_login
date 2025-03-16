from login.models import Usuario

from django.shortcuts import render, redirect

def menu_view(request):
    usuarios = Usuario.objects.all().order_by('-fecha_creacion')  # Ordena por fecha de creación
    return render(request, 'menu.html', {'usuarios': usuarios})
