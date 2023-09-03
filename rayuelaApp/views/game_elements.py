
from django.shortcuts import render, redirect
from rayuelaApp.models.project import Project
from rayuelaApp.models.challenge import Challenge
from rayuelaApp.models.game_element import GameElement
from django.contrib import messages
from rayuelaApp.models.badge import Badge
from rayuelaApp.models.user import User
from rayuelaApp.models.criteria import Criteria
from rayuelaApp.utils.System import System

def view_game_elements(request,ok=False):  
    if System.is_logged(request):
          if System.is_player(request):
              if request.method != 'POST':
                project=Project.objects.get(id__exact=request.session['old'])   
              else:
                project=Project.objects.get(id__exact=request.POST['id'])  
              return render(request, 'rayuelaApp/game_elements/views_game_elements.html',{'nav':'block','view_game_elements':System.get_navbar_color,'badges':Badge.objects.filter(project=project,public=True).exclude(user_actives = User.objects.get(id=request.session['id'])).all(),'challenges':Challenge.objects.filter(project=project,public=True).exclude(user_actives = User.objects.get(id=request.session['id'])).all(),'name':project.get_name(),'my_badges':Badge.objects.filter(user_actives=User.objects.get(id=request.session['id']),project=project,public=True).all(), 'my_challenges': Challenge.objects.filter(user_actives=User.objects.get(id=request.session['id']),project=project,public=True).all(), 'criterias':Criteria.objects.all()})
          return redirect('home')
    return redirect('index')  

def change_state(request):
    if System.is_logged(request):
          if System.is_admin(request):
            ge=GameElement.objects.get_subclass(id=request.POST['ge_id'])
            ge.change_state()     
            messages.success(request,' %s  %s con éxito'  % (ge.get_name(),ge.get_state()))
            request.session['old']=ge.get_id_project()
            return redirect('game_elements_project')
          return redirect('home')
    return redirect('index')  

def modify(request,ok=False):
  if System.is_logged(request):
        if System.is_admin(request):
          if not ok:
            id_= request.POST['ge_id_']
          else:
            id_=request.POST['id']
          ge=GameElement.objects.get_subclass(id=id_)
          areas=ge.get_project().get_area().projectsubarea_set.all()
          time_restrictions=ge.get_project().get_time_restrictions().all()
          if isinstance(ge, Challenge):
            return render(request, 'rayuelaApp/game_elements/modify_challenge.html',{'nav':'block','modify_challenge':System.get_navbar_color,'challenge':ge, 'areas':areas,'time_restrictions':time_restrictions})
          return render(request, 'rayuelaApp/game_elements/modify_badge.html',{'nav':'block','modify_badge':System.get_navbar_color,'badge':ge,'areas':areas,'time_restrictions':time_restrictions,'badges':Badge.objects.filter(project_id=ge.get_id_project()).all()})
        return redirect('home')
  return redirect('index')  