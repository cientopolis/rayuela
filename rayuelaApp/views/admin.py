from django.shortcuts import redirect, render
from rayuelaApp.models.user import User
from rayuelaApp.models.role import Role
from rayuelaApp.utils.System import System
from django.contrib import messages
from werkzeug.security import generate_password_hash


def register_admin(request):
  
    if User.objects.filter(email__exact=request.POST['email']).exists() or  User.objects.filter(username__exact=request.POST['username']).exists():
        messages.error(request,'Nombre de usuario/email ya registrado')
        return redirect('create_admin')
    if not request.POST['email'] or not request.POST['username'] or not request.POST['password'] or not request.POST['repeat_password'] or not request.POST['name'] or (request.POST['password'] != request.POST['repeat_password']):
        if (request.POST['password'] != request.POST['repeat_password']):
            messages.error(request,'Las contraseñas no coinciden')
        else:
            messages.error(request,'Todos los campos deben estar completos')
        return redirect('create_admin')
        
    user=User(email=request.POST['email'],username=request.POST['username'],complete_name=request.POST['name'],role_id=Role.objects.get(name='ADMIN'),password=generate_password_hash(request.POST['password'], 'sha256', 10))
    user.save()
    messages.success(request,'¡Administrador dado de alta con éxito')
    return redirect('create_admin')


def create_admin(request):
     if System.is_logged(request):
          if System.is_root(request):
            return render (request,'rayuelaApp/create_admin.html',{'nav':'block','create_admin':System.get_navbar_color})
          return redirect('home')
     return redirect('index')  


