from django.shortcuts import redirect, render, reverse
from django.contrib import messages

from rayuelaApp.models.project import Project
from rayuelaApp.models.badge import Badge
from rayuelaApp.models.badge_requirement import BadgeRequirement
from rayuelaApp.models.leaderboard import Leaderboard
from rayuelaApp.forms import BadgeForm
from rayuelaApp.models.task_type import TaskType
from rayuelaApp.models.time_restriction import TimeRestriction
from rayuelaApp.models.project_subarea import ProjectSubArea
from rayuelaApp.utils.System import System
from rayuelaApp.models.score_allocation_strategy import ScoreAllocationStrategy

'''
==========================
Reglas de juego - General
==========================
'''

def view_game_rules(request, id):
    if System.is_logged(request):
        if System.is_admin(request):
           return render(request, 'rayuelaApp/game/game_rules.html', {'nav': 'block', 'project': Project.objects.get(id=id), 'badges': Badge.objects.filter(project=id, available=True), 'scores': ScoreAllocationStrategy.objects.filter(project=id), 'leaderboard': Leaderboard.objects.filter(project=id)})
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
           return render(request, 'rayuelaApp/game/create_badge.html', {'nav': 'block', 'project': Project.objects.get(id=id), 'badges': Badge.objects.filter(project=id, available=True), 'sub_areas': ProjectSubArea.objects.filter(area=Project.objects.get(id=id).area)})
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

def delete_badge(request, project_id, badge_id):
    if System.is_logged(request):
        if System.is_admin(request):
            badge = Badge.objects.get(id=badge_id)
            requirements = BadgeRequirement.objects.filter(badge_id=badge_id)
            if requirements:
                for requirement in requirements:
                    requirement.badge_id=0
                    requirement.save()
            badge.available = False
            badge.save()
            messages.success(request, 'Se ha eliminado correctamente')
            return redirect(reverse('game_rules', kwargs={'id': project_id}))
        return redirect('home')
    return redirect('index')

def modify_badge(request, project_id, badge_id):
    if System.is_logged(request):
        if System.is_admin(request):
           return render(request, 'rayuelaApp/game/modify_badge.html', {'nav': 'block', 'project': Project.objects.get(id=project_id), 'badges': Badge.objects.filter(project=project_id, available=True), 'sub_areas': ProjectSubArea.objects.filter(area=Project.objects.get(id=project_id).area), 'badge': Badge.objects.get(id=badge_id)})
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
                        requirements.time_restriction = TimeRestriction.objects.get(id=request.POST['select_time_restrictions'])
                        requirements.badge_id = request.POST['requirements_badge_id']
                        requirements.times = request.POST['requirements_times']
                        requirements.save()
                    else:
                        requirements = BadgeRequirement(time_restriction=TimeRestriction.objects.get(id=request.POST['select_time_restrictions']), badge_id=request.POST['requirements_badge_id'], times=request.POST['requirements_times'])
                        requirements.save()
                        badge.requirements = requirements
                else:
                    if badge.requirements.sub_area:
                        requirements = BadgeRequirement.objects.get(id=badge.requirements.id)
                        requirements.sub_area = ProjectSubArea.objects.get(id=request.POST['select_areas'])
                        requirements.badge_id = request.POST['requirements_badge_id']
                        requirements.times = request.POST['requirements_times']
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
                if not request.POST.get('is_contribution'):
                    score = ScoreAllocationStrategy(project=Project.objects.get(id=request.POST['project_id']), name=request.POST.get('name'), checkin=True, points=request.POST.get('points'))
                else:
                    if criterion == "task_type":
                        score = ScoreAllocationStrategy(project=Project.objects.get(id=request.POST['project_id']), name=request.POST.get('name'), task_type=TaskType.objects.get(id=request.POST.get('select_task_types')),
                                                 points=request.POST.get('points'))
                    elif criterion == "time_restriction":
                        score = ScoreAllocationStrategy(project=Project.objects.get(id=request.POST['project_id']), name=request.POST.get('name'), time_restriction=TimeRestriction.objects.get(id=request.POST.get('select_time_restrictions')),
                                                 points=request.POST.get('points'))
                    else:
                        score = ScoreAllocationStrategy(project=Project.objects.get(id=request.POST['project_id']), name=request.POST.get('name'), sub_area=ProjectSubArea.objects.get(id=request.POST.get('select_areas')),
                                                 points=request.POST.get('points'))
                score.save()
                messages.success(request, 'Se ha creado correctamente')
                return redirect(reverse('game_rules', kwargs={'id': request.POST['project_id']}))
        return redirect ('home')
    return redirect ('index')