
from django.shortcuts import redirect, render
import json
from rayuelaApp.models.project import Project
from rayuelaApp.models.user import User
from rayuelaApp.models.role import Role
from rayuelaApp.models.project_area import ProjectArea
from rayuelaApp.models.challenge import Challenge
from rayuelaApp.models.badge import Badge
from rayuelaApp.utils.System import System
from django.contrib import messages
from rayuelaApp.forms import ProjectForm
import geopandas as gpd


def create_project(request):
     if System.is_logged(request):
          if System.is_root(request):
            return render (request,'rayuelaApp/projects/create_project.html',{'nav':'block','create_project':System.get_navbar_color, 'admins':User.objects.filter(role_id__exact=Role.objects.get(name='ADMIN'))})
          redirect('home')
     return redirect('index')  

def register_project(request):    
     if System.is_logged(request):
          if System.is_root(request):        
            if not len(request.POST.getlist('select[]')) or not request.POST['name']:
               messages.error(request,'Debe ingresar todos los campos')
               return redirect('create_project') 
            project = Project(name=request.POST['name'])
            project.save()
            project.add_admins(request.POST.getlist('select[]'))
            messages.success(request,'¡Proyecto creado con éxito¡')
            return redirect('create_project') 
          return redirect('home')
     return redirect('index')  

def modify_project(request):
    if System.is_logged(request):
          if System.is_admin(request):
               if request.method == 'POST':
                    return render (request,'rayuelaApp/projects/modify_project.html',{'nav':'block','modify_project':System.get_navbar_color, 'project':Project.objects.get(id__exact=request.POST.get('id')),'areas':ProjectArea.objects.all(),'time_restrictions':Project.objects.get(id__exact=request.POST.get('id')).time_restriction.all()})
               else:
                    messages.success(request,'¡RT Creado con éxito!')
                    return render (request,'rayuelaApp/projects/modify_project.html',{'nav':'block','modify_project':System.get_navbar_color, 'project':Project.objects.get(id__exact=request.session['project_id']),'areas':ProjectArea.objects.all(),'time_restrictions':Project.objects.get(id__exact=request.session['project_id']).time_restriction.all()})
          return redirect('home')
    return redirect('index') 


def edit_project(request):
     if System.is_logged(request):
          if System.is_admin(request):                              
                if not request.POST.get('name') or not request.POST.get('description')  :
                     messages.error(request,'Debe ingresar todos los campos')
                     return modify_project(request)              
                project=Project.objects.get(id__exact=request.POST['id'])              
                project.modify(request.POST['name'],request.POST['description'],request.POST.get('checkbox')) 
                if request.FILES.get('area'):                               
                    df = gpd.read_file(request.FILES.get('area'), driver='GeoJSON')   
                    area=json.loads(df.to_json())
                    p_area= ProjectArea(name=area['type'])
                    p_area.save()
                    p_area.add_subareas(area['features'])
                    project.add_area(p_area)              
                project.add_time_restrictions(request.POST.getlist('time_restriction[]'))
                project.save()           
                form = ProjectForm(data=request.POST, files=request.FILES, instance=project)
                form.procces(project.get_image_path())
                if request.POST['bool'] == 'true':
                    request.session['project_id']=request.POST['id']
                    return redirect ('create_time_restriction')
                messages.success(request,'Proyecto %s modificado con éxito ' % (project.get_name()))
          return redirect('home') 
     return redirect('index')

def game_elements_project(request):
     if System.is_logged(request):
          if System.is_admin(request): 
               if request.method != 'POST' :
                  project_=  Project.objects.get(id__exact= request.session['old'])  
                  
               else:
                  project_=Project.objects.get(id__exact=request.POST['id'])                             
               return render (request,'rayuelaApp/game_elements/game_elements_project.html',{'nav':'block','game_elements_project':System.get_navbar_color, 'project_name':project_.get_name(),'challenges':Challenge.objects.filter(project=project_),'badges': Badge.objects.filter(project=project_)})
          return redirect('home') 
     return redirect('index')

def see_all_projects(request):
     if System.is_logged(request):
          if System.is_player(request):         
               return render (request,'rayuelaApp/projects/see_all_projects.html',{'nav':'block','see_all_projects':System.get_navbar_color, 'projects':Project.objects.filter(avaliable=True).exclude(user__id=request.session['id']) } )
          elif System.is_root(request):

               return render (request,'rayuelaApp/projects/see_all_projects.html',{'nav':'block','see_all_projects':System.get_navbar_color, 'projects':Project.objects.all() } )
          return redirect('home') 
     return redirect('index')

def asign_project(request):
     if System.is_logged(request):
          if System.is_player(request): 
               project= Project.objects.get(id=request.POST['project_id'])
               User.objects.get(id=request.session['id']).add_project(project)
               messages.success(request,'¡Proyecto %s añadido exitosamente!' % (project.get_name()))  
               return see_all_projects(request) 
          return redirect('home') 
     return redirect('index')

def disjoin_project(request):
     if System.is_logged(request):
          if System.is_player(request): 
              project=Project.objects.get(id=request.POST['project_id'])   
              User.objects.get(id=request.session['id']).disjoin_project(project)
              messages.success(request,'¡Proyecto %s eliminado exitosamente!' % (project.get_name()))  
              return redirect ('my_projects')
          return redirect('home') 
     return redirect('index')

def modify_project_root(request):
    if System.is_logged(request):
          if System.is_root(request):
               if request.method == 'POST':
                    return render (request,'rayuelaApp/projects/modify_project_root.html',{ 'project':Project.objects.get(id__exact=request.POST.get('project_id')),'admins':User.objects.filter(role_id__exact=Role.objects.get(name='ADMIN'))})
               else:
                    return render (request,'rayuelaApp/projects/modify_project_root.html',{ 'project':Project.objects.get(id__exact=request.session['project_id']),'admins':User.objects.filter(role_id__exact=Role.objects.get(name='ADMIN'))})
          return redirect('home')
    return redirect('index') 

def process_modify_project(request):    
     if System.is_logged(request):
          request.session['project_id']=request.POST.get('project_id')
          if System.is_root(request):   
                
            if not len(request.POST.getlist('select[]')) or not request.POST['name']:
               messages.error(request,'Debe ingresar todos los campos')
               return redirect ('modify_project_root')
            project = Project(id=request.POST['project_id'])
            project.set_name(request.POST['name'])
            project.update_admins(request.POST.getlist('select[]'))           
            messages.success(request,'¡Proyecto actualizado con éxito¡')
            return redirect ('modify_project_root')
          return redirect('home')
     return redirect('index')  

