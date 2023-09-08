

from django.shortcuts import redirect, render
from django import template
from rayuelaApp.models.role import Role
from rayuelaApp.models.user import User
from rayuelaApp.models.project import Project
from rayuelaApp.models.challenge import Challenge
from rayuelaApp.models.badge import Badge
from rayuelaApp.models.criteria import Criteria
from rayuelaApp.forms import UserForm
from rayuelaApp.utils.System import System
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from werkzeug.security import generate_password_hash,check_password_hash





register = template.Library()


def index(request):
    if System.is_logged(request):
        return redirect('home')   
    return render(request, 'rayuelaApp/index.html')

def register(request):
    if System.is_logged(request):
        return redirect('home')   
    return render(request, 'rayuelaApp/register.html')

def home(request):
    if System.is_logged(request):
        if System.is_admin(request):
            projects=Project.objects.filter(admins__id=request.session['id']).order_by('-id')
        else:
            projects=User.objects.get(id=request.session['id']).get_projects().all()
        return render(request, 'rayuelaApp/home.html',{'projects':projects})
    return redirect('index')
    
    
def login(request):     
    
    if not request.POST['email'] or not request.POST['password']:
        messages.error(request,'Debe ingresar todos los campos')
        return redirect('index')    
    try:  
        if '@' in request.POST['email']:
            user=User.objects.get( email__iexact=request.POST['email'])
        else:
            user=User.objects.get( username__iexact=request.POST['email'])    
        if not check_password_hash(user.get_password(),request.POST['password']):
           raise ObjectDoesNotExist 
    except ObjectDoesNotExist:

        messages.error(request,'Usuario/Email o contraseña incorrectos')
        return redirect('index')
    System.set_session(request,user)        
    return user_verificate(request,True,user)

def user_verificate(request,ok=False,user=False):  
    try:
        if not user.is_verified():
            if ok:  
                System.f_send_mail(user)               
            return redirect('verificate')
        return redirect('home')
    except:
        return redirect('index')   
    

def logout(request):
        System.logout(request)       
        return redirect('index')
    
def register_user(request):
    if System.is_logged(request):    
        return redirect('home')       
    if User.objects.filter(email__exact=request.POST['email']).exists() or  User.objects.filter(username__exact=request.POST['username']).exists():
        messages.error(request,'Nombre de usuario/email ya utilizado')
        logout(request)
        return redirect('register')
    if not request.POST['email'] or not request.POST['username'] or not request.POST['password'] or not request.POST['repeat_password'] or not request.POST['name'] or (request.POST['password'] != request.POST['repeat_password']):
        if (request.POST['password'] != request.POST['repeat_password']):
            messages.error(request,'Las contraseñas no coinciden')
        else:
            messages.error(request,'Todos los campos deben estar completos')
        return redirect('register')
        
    user=User(email=request.POST['email'],username=request.POST['username'],complete_name=request.POST['name'],role_id=Role.objects.get(name='PLAYER'),password=generate_password_hash(request.POST['password'], 'sha256', 10))
    user.save()
    System.set_session(request,user)  
    return user_verificate(request,True,user)

def verificate(request):
    return render (request,'rayuelaApp/verificate/verificate.html')

def activate_account(request):       
    user_id=System.decode_token(request.GET.get('token'))
    if user_id:
        user=User.objects.get(id=user_id)
        user.change_verified()
        logout(request)
        request.session['av']=True 
        return redirect('active_account')
        

def active_account(request):
    try:
        del request.session['av']
        return render (request,'rayuelaApp/verificate/active_account.html')
    except KeyError:
        return redirect('index')  




def see_my_game_elements(request):
    if System.is_logged(request):
        if System.is_player(request):       
            return render(request, 'rayuelaApp/game_elements/my_game_elements.html',{'nav':'block','see_my_game_elements':System.get_navbar_color,'my_badges':Badge.objects.filter(user_actives=User.objects.get(id=request.session['id']),public=True).all(),'my_challenges':Challenge.objects.filter(user_actives=User.objects.get(id=request.session['id']),public=True).all(),'criterias':Criteria.objects.all()})
        return redirect('home')  
    return redirect('index')   

def edit_profile(request):
    if System.is_logged(request):
        if System.is_player(request):    
            return render(request, 'rayuelaApp/user/edit_profile.html',{'edit_profile':System.get_navbar_color })
        return redirect('home')  
    return redirect('index')      

def process_edit_profile(request):
    if System.is_logged(request):
        if System.is_player(request):    
            if not request.POST['name'] or not request.POST['email'] or not request.POST['password'] or not request.POST['repeat_password']:
                messages.error(request,'Los campos deben estar completos')
                return edit_profile(request)
            elif User.objects.filter(email__exact=request.POST['email']).exclude(id=request.session['id']).exists():
                messages.error(request,'Ya existe un usuario con ese email')
                return edit_profile(request)
            elif request.POST['password'] != request.POST['repeat_password']:
                messages.error(request,'Las contraseñas deben ser iguales')
                return edit_profile(request)
            user=User.objects.get(id__exact=request.session['id'])          
            user.update_data(request.POST['name'],request.POST['email'],request.POST['password']) 
            form = UserForm(data=request.POST, files=request.FILES, instance=user)
            form.procces(user.get_profile_image_path())
            System.set_session(request,user)
            messages.success(request,'¡Datos actualizados con éxito!')
            return edit_profile(request)
        return redirect('home')  
    return redirect('index')   


def my_projects(request):
    if System.is_logged(request):
        if System.is_player(request):   
             return render(request, 'rayuelaApp/projects/my_projects.html',{'nav':'block','my_projects':System.get_navbar_color,'projects':Project.objects.filter(user__id=request.session['id']) })
        return redirect('home')  
    return redirect('index') 