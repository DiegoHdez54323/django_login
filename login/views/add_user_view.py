from django.shortcuts import render, redirect
from login.models import Usuario

def add_user_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')

        Usuario.objects.create(nombre=nombre, correo=correo, contraseña=contraseña)
        return redirect('menu')