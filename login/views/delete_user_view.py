from django.shortcuts import redirect, get_object_or_404
from login.models import Usuario

def delete_user_view(request, user_id):
    usuario = get_object_or_404(Usuario, id=user_id)
    usuario.delete()
    return redirect('menu')