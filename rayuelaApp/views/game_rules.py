from django.shortcuts import redirect, render, reverse

from rayuelaApp.models.project import Project
from rayuelaApp.models.badge import Badge
from rayuelaApp.models.score import Score
from rayuelaApp.models.score_allocation_strategy import ScoreByCheckin, ScoreByTaskType, ScoreByTimerRestriction, \
    ScoreByArea
from rayuelaApp.models.project_subarea import ProjectSubArea
from rayuelaApp.models.badge_requirement import BadgeRequirement
from rayuelaApp.models.leaderboard import Leaderboard
from rayuelaApp.forms import BadgeForm
from rayuelaApp.models.task_type import TaskType
from rayuelaApp.models.time_restriction import TimeRestriction
from rayuelaApp.models.project_subarea import ProjectSubArea
from rayuelaApp.utils.System import System
from django.contrib import messages

'''
==========================
Reglas de juego - General
==========================
'''

def view_game_rules(request, id):
    if System.is_logged(request):
        if System.is_admin(request):
           return render(request, 'rayuelaApp/game/game_rules.html', {'nav': 'block', 'project': Project.objects.get(id=id), 'badges': Badge.objects.filter(project=id, available=True), 'scores': Score.objects.filter(project=id), 'leaderboard': Leaderboard.objects.filter(project=id)})
        return redirect('home')
    return redirect('index')

'''
==========================
    Tabla de posiciones
==========================
'''

def process_leaderboard(request):
    if System.is_logged(request):
        if System.is_admin(request):
            request.session['project_id']=request.POST['project_id']
            order_by_points = True
            if request.POST['select_leaderboard'] == 'badges':
                order_by_points = False
            if len(Leaderboard.objects.filter(project=request.POST['project_id'])) > 0:
               leaderboard = Leaderboard.objects.get(project=request.POST['project_id'])
               leaderboard.order_by_points = order_by_points
            else:
               leaderboard = Leaderboard(project=Project.objects.get(id=request.POST['project_id']), order_by_points=order_by_points)
            leaderboard.save()
            messages.success(request, 'Se ha actualizado correctamente')
            return redirect(reverse('game_rules', kwargs={'id': request.POST['project_id']}))
        return redirect ('home')
    return redirect ('index')

'''
==========================
        Insignias
==========================
'''

def create_badge(request, id):
    if System.is_logged(request):
        if System.is_admin(request):
           return render(request, 'rayuelaApp/game/create_badge.html', {'nav': 'block', 'project': Project.objects.get(id=id), 'badges': Badge.objects.filter(project=id), 'sub_areas': ProjectSubArea.objects.filter(area=Project.objects.get(id=id).area)})
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
                criterion = request.POST.get('criterion')
                if criterion == "task_type":
                    requirements = BadgeRequirement(task_type=TaskType.objects.get(id=request.POST['select_task_types']), badge_id=request.POST['requirements_badge_id'], times=request.POST['requirements_times'])
                    requirements.save()
                elif criterion == "time_restriction":
                    requirements = BadgeRequirement(time_restriction=TimeRestriction.objects.get(id=request.POST['select_time_restrictions']), badge_id=request.POST['requirements_badge_id'], times=request.POST['requirements_times'])
                    requirements.save()
                else:
                    requirements = BadgeRequirement(sub_area=ProjectSubArea.objects.get(id=request.POST['select_areas']), badge_id=request.POST['requirements_badge_id'], times=request.POST['requirements_times'])
                    requirements.save()
                badge = Badge(project=Project.objects.get(id=request.POST['project_id']), name=request.POST['name'], description=request.POST['description'], requirements=requirements)
                badge.save()
                form = BadgeForm(data=request.POST, files=request.FILES, instance=badge)
                form.procces(badge.get_path_image())
                messages.success(request, 'Se ha creado correctamente')
                return redirect(reverse('game_rules', kwargs={'id': request.POST['project_id']}))
        return redirect ('home')
    return redirect ('index')

def modify_badge(request, project_id, badge_id):
    if System.is_logged(request):
        if System.is_admin(request):
           return render(request, 'rayuelaApp/game/modify_badge.html', {'nav': 'block', 'project': Project.objects.get(id=project_id), 'badges': Badge.objects.filter(project=project_id), 'sub_areas': ProjectSubArea.objects.filter(area=Project.objects.get(id=project_id).area), 'badge': Badge.objects.get(id=badge_id)})
        return redirect('home')
    return redirect('index')

def process_modify_badge(request):
    if System.is_logged(request):
        if System.is_admin(request):
            request.session['project_id']=request.POST['project_id']
            request.session['badge_id'] = request.POST['badge_id']
            if not request.POST['name'] or not request.POST['description'] or not request.POST['requirements_badge_id'] or not request.POST['requirements_times']:
                messages.error(request, 'Debe ingresar todos los campos')
                return modify_badge(request, request.session['project_id'], request.session['badge_id'])
            else:
                badge = Badge.objects.get(id=request.session['badge_id'])
                criterion = request.POST.get('criterion')
                if criterion == "task_type":
                    if badge.requirements.task_type:
                        requirements = BadgeRequirement.objects.get(id=badge.requirements.id)
                        requirements.task_type = TaskType.objects.get(id=request.POST['select_task_types'])
                        requirements.badge_id = request.POST['requirements_badge_id']
                        requirements.times = request.POST['requirements_times']
                        requirements.save()
                    else:
                        requirements = BadgeRequirement(task_type=TaskType.objects.get(id=request.POST['select_task_types']), badge_id=request.POST['requirements_badge_id'], times=request.POST['requirements_times'])
                        requirements.save()
                        badge.requirements = requirements
                elif criterion == "time_restriction":
                    if badge.requirements.time_restriction:
                        requirements = BadgeRequirement.objects.get(id=badge.requirements.id)
                        badge.requirements.time_restriction = TimeRestriction.objects.get(id=request.POST['select_time_restrictions'])
                        badge.requirements.badge_id = request.POST['requirements_badge_id']
                        badge.requirements.times = request.POST['requirements_times']
                        requirements.save()
                    else:
                        requirements = BadgeRequirement(time_restriction=TimeRestriction.objects.get(id=request.POST['select_time_restrictions']), badge_id=request.POST['requirements_badge_id'], times=request.POST['requirements_times'])
                        requirements.save()
                        badge.requirements = requirements
                else:
                    if badge.requirements.sub_area:
                        requirements = BadgeRequirement.objects.get(id=badge.requirements.id)
                        badge.requirements.sub_area = ProjectSubArea.objects.get(id=request.POST['select_areas'])
                        badge.requirements.badge_id = request.POST['requirements_badge_id']
                        badge.requirements.times = request.POST['requirements_times']
                        requirements.save()
                    else:
                        requirements = BadgeRequirement(sub_area=ProjectSubArea.objects.get(id=request.POST['select_areas']), badge_id=request.POST['requirements_badge_id'], times=request.POST['requirements_times'])
                        requirements.save()
                        badge.requirements = requirements
                badge.name=request.POST['name']
                badge.description=request.POST['description']
                badge.save()
                if request.FILES:
                    form = BadgeForm(data=request.POST, files=request.FILES, instance=badge)
                    form.procces(badge.get_path_image())
                messages.success(request, 'Se ha modificado correctamente')
                return redirect(reverse('game_rules', kwargs={'id': request.POST['project_id']}))
        return redirect ('home')
    return redirect ('index')

'''
==========================
         Puntajes
==========================
'''

def create_score(request, id):
    if System.is_logged(request):
        if System.is_admin(request):
           return render(request, 'rayuelaApp/game/create_score.html', {'nav': 'block', 'project': Project.objects.get(id=id), 'sub_areas': ProjectSubArea.objects.filter(area=Project.objects.get(id=id).area)})
        return redirect('home')
    return redirect('index')

def process_score(request):
    if System.is_logged(request):
        if System.is_admin(request):
            request.session['project_id']=request.POST['project_id']
            if not request.POST['name']:
                messages.error(request, 'Debe ingresar todos los campos')
                return create_score(request, request.session['project_id'])
            else:
                criterion = request.POST.get('criterion')
                # TODO:
                #  Quitar criterian_id=0 (ver si por default alcanza)
                #  Averiguar si ya existe un checkin ( con contribution_id=0 u otra forma) y en ese caso editarlo en lugar de crearlo
                #  Usar if/else similar al de process_leaderboard
                if not request.POST.get('is_contribution'):
                    checkin = ScoreByCheckin(name=request.POST.get('name'), criterian_id=0, points=request.POST.get('points'))
                    checkin.save()
                    score = Score(project=Project.objects.get(id=request.POST['project_id']))
                    score.save()
                    score.add_score(checkin)
                else:
                    # TODO: hay que identificar de qué criterio era, sino no se puede obtener luego
                    if criterion == "task_type":
                        task_type = ScoreByTaskType(name=request.POST.get('name'), criterian_id=request.POST.get('select_task_types'),
                                                 points=request.POST.get('points'))
                        score = Score(project=Project.objects.get(id=request.POST['project_id']))
                        task_type.save()
                        score.save()
                        score.add_score(task_type)
                    elif criterion == "time_restriction":
                        time_restriction = ScoreByTimerRestriction(name=request.POST.get('name'), criterian_id=request.POST.get('select_time_restrictions'),
                                                 points=request.POST.get('points'))
                        score = Score(project=Project.objects.get(id=request.POST['project_id']))
                        time_restriction.save()
                        score.save()
                        score.add_score(time_restriction)
                    else:
                        area = ScoreByArea(name=request.POST.get('name'), criterian_id=request.POST.get('select_areas'),
                                                 points=request.POST.get('points'))
                        score = Score(project=Project.objects.get(id=request.POST['project_id']))
                        area.save()
                        score.save()
                        score.add_score(area)
                messages.success(request, 'Se ha creado correctamente')
                return redirect(reverse('game_rules', kwargs={'id': request.POST['project_id']}))
        return redirect ('home')
    return redirect ('index')