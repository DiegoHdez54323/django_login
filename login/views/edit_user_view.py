from django.shortcuts import redirect, get_object_or_404
from login.models import Usuario

def edit_user_view(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        usuario = get_object_or_404(Usuario, id=user_id)
        
        usuario.nombre = request.POST['nombre']
        usuario.correo = request.POST['correo']

        nueva_contraseña = request.POST['contraseña']
        if nueva_contraseña:  # Solo actualiza la contraseña si se introduce una nueva
            usuario.contraseña = nueva_contraseña
        
        usuario.save()
    
    return redirect('menu')