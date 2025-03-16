from django.shortcuts import render, redirect
from django.contrib import messages

from login.models import Usuario

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Primero busca al usuario por nombre
            user = Usuario.objects.get(nombre=username)

            # Luego, compara la contraseña manualmente
            if user.contraseña == password:
                return redirect('menu')
            else:
                messages.error(request, 'Contraseña incorrecta')

        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario no encontrado')

    return render(request, 'login.html') 
