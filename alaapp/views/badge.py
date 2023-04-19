
from django.shortcuts import redirect, render
from alaapp.models.user import  User 
from alaapp.models.project import Project
from alaapp.models.project_subarea import ProjectSubArea
from alaapp.models.time_restriction import TimeRestriction
from alaapp.views import game_elements
from alaapp.utils.System import System
from alaapp.models.badge import Badge
from alaapp.models.assignment import Assignment
from django.contrib import messages
from alaapp.forms import BadgeForm





def badge(request):
    if System.is_logged(request):
          if System.is_admin(request):
              return render(request, 'alaapp/game_elements/create_badge.html',{'nav':'block','create_badge':System.get_navbar_color,'badges':Badge.objects.all(),'projects':Project.objects.filter(admins=request.session['id'])})
          return redirect('home')  
    return redirect('index') 

def process_badge(request):
    if System.is_logged(request):
          if System.is_admin(request):
              if not request.POST['name'] or not request.POST['area'] or not request.POST['project'] or not request.POST['time_restriction'] or not request.POST['goal']:
                  messages.error(request,'Debe ingresar todos los campos') 
                  return badge(request)               
              elif Badge.objects.filter(name__iexact=request.POST['name'],project=Project.objects.get(id__exact=request.POST['project'])).exists():
                  messages.error(request,'Ya hay una insignia con ese nombre') 
                  return badge(request)   
              badge_= Badge(name=request.POST['name'],area=ProjectSubArea.objects.get(id__exact=request.POST['area']),time_restriction=TimeRestriction.objects.get(id__exact=request.POST['time_restriction']),goal=request.POST['goal'],owner=User.objects.get(id__exact=request.session['id']),project=Project.objects.get(id__exact=request.POST['project']))                
              badge_.add_parent(int(request.POST['select']))    
              badge_.save()            
              form = BadgeForm(data=request.POST, files=request.FILES, instance=badge_)
              form.procces(badge_.get_path_image())
              messages.success(request,'Se ha creado correctamente')
              return badge(request)   
          return redirect('home')  
    return redirect('index') 

def asign_badge(request):
    if System.is_logged(request):
          if System.is_player(request):
            badge= Badge.objects.get(id=request.POST['badge_id'])
            user = User.objects.get(id=request.session['id'])
            user.add_gamelement_active(badge)
            bp = Assignment(user=user,game_element=badge)
            bp.save()
            messages.success(request,'Insignia %s  asignado con éxito'  % (badge.get_name()))
            request.session['old']=badge.get_id_project()
            return redirect ('view_game_elements')
          return redirect('home')  
    return redirect('index')  

def modify_badge(request):
    if System.is_logged(request):
          if System.is_admin(request):  
                try:
                    request.POST['name']
                except:
                    return redirect ('home')
                if not request.POST['name'] or not request.POST['area'] or  not request.POST['time_restriction'] or not request.POST['goal']:
                    messages.error(request,'Debe ingresar todos los campos')
                    return game_elements.modify(request,True)               
                elif Badge.objects.filter(name__iexact=request.POST['name'],project=Project.objects.get(id__exact=request.POST['id_project'])).exclude(id__exact=request.POST['id']).exists():
                    messages.error(request,'Ya hay una insignia con ese nombre')
                    return game_elements.modify(request,True)       
                else: 
                    badge_=Badge.objects.get(id__exact=request.POST['id'])
                    badge_.update(request.POST['name'],ProjectSubArea.objects.get(id__exact=request.POST['area']),TimeRestriction.objects.get(id__exact=request.POST['time_restriction']),request.POST['goal'],int(request.POST['select']))             
                    form = BadgeForm(data=request.POST, files=request.FILES, instance=badge_)
                    form.procces(badge_.get_path_image())
                    messages.success(request,'Insignia modificada correctamente')
                return game_elements.modify(request,True)     
          return redirect('home')  
    return redirect('index')  