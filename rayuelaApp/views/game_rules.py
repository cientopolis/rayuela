from django.shortcuts import redirect, render, reverse

from rayuelaApp.models.project import Project
from rayuelaApp.models.badge import Badge
from rayuelaApp.models.badge_requirement import BadgeRequirement
from rayuelaApp.forms import BadgeForm
from rayuelaApp.models.task_type import TaskType
from rayuelaApp.utils.System import System
from django.contrib import messages

def view_game_rules(request, id):
    if System.is_logged(request):
        if System.is_admin(request):
           return render(request, 'rayuelaApp/game/game_rules.html', {'nav': 'block', 'project': Project.objects.get(id=id), 'badges': Badge.objects.filter(project=id)})
        return redirect('home')
    return redirect('index')

def create_badge(request, id):
    if System.is_logged(request):
        if System.is_admin(request):
           return render(request, 'rayuelaApp/game/create_badge.html', {'nav': 'block', 'project': Project.objects.get(id=id), 'badges': Badge.objects.filter(project=id)})
        return redirect('home')
    return redirect('index')

def process_badge(request):
    if System.is_logged(request):
        if System.is_admin(request):
            request.session['project_id']=request.POST['project_id']
            if not request.POST['name'] or not request.POST['description'] or not request.POST['requirements_badge_id'] or not request.POST['requirements_times']:
                messages.error(request, 'Debe ingresar todos los campos')
                return create_badge(request, request.session['project_id'])
            else:
                requirements = BadgeRequirement(task_type=TaskType.objects.get(id=request.POST['requirements_task_type']), badge_id=request.POST['requirements_badge_id'], times=request.POST['requirements_times'])
                requirements.save()
                badge = Badge(project=Project.objects.get(id=request.POST['project_id']), name=request.POST['name'], description=request.POST['description'], requirements=requirements)
                badge.save()
                form = BadgeForm(data=request.POST, files=request.FILES, instance=badge)
                form.procces(badge.get_path_image())
                messages.success(request, 'Se ha creado correctamente')
                return redirect(reverse('game_rules', kwargs={'id': request.POST['project_id']}))
                #return view_game_rules(request, request.POST['project_id'])
        return redirect ('home')
    return redirect ('index')

# def modify(request,ok=False):
#   if System.is_logged(request):
#         if System.is_admin(request):
#           if not ok:
#             id_= request.POST['ge_id_']
#           else:
#             id_=request.POST['id']
#           ge=GameElement.objects.get_subclass(id=id_)
#           areas=ge.get_project().get_area().projectsubarea_set.all()
#           time_restrictions=ge.get_project().get_time_restrictions().all()
#           if isinstance(ge, Challenge):
#             return render(request, 'rayuelaApp/game_elements/modify_challenge.html',{'nav':'block','modify_challenge':System.get_navbar_color,'challenge':ge, 'areas':areas,'time_restrictions':time_restrictions})
#           return render(request, 'rayuelaApp/game_elements/modify_badge.html',{'nav':'block','modify_badge':System.get_navbar_color,'badge':ge,'areas':areas,'time_restrictions':time_restrictions,'badges':Badge.objects.filter(project_id=ge.get_id_project()).all()})
#         return redirect('home')
#   return redirect('index')