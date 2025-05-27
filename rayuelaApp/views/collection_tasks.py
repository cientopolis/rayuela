from django.shortcuts import redirect, reverse, render
from django.contrib import messages

from rayuelaApp.models.task_type import TaskType
from rayuelaApp.models.time_restriction import TimeRestriction
from rayuelaApp.utils.System import System

from rayuelaApp.models.collection_task import CollectionTask
from rayuelaApp.models.project import Project
from rayuelaApp.models.project_subarea import ProjectSubArea

def automatic_task_generation(request, id):
    if System.is_logged(request):
        if System.is_admin(request):
            if request.method == 'POST':
                project = Project.objects.get(id=id)
                project.automatic_task_generation()
                return redirect(reverse('collection_tasks', kwargs={'id': id}))
        return redirect ('home')
    return redirect ('index')

def delete_collection_task(request, project_id, collection_task_id):
    if System.is_logged(request):
        if System.is_admin(request):
            collection_task = CollectionTask.objects.get(id=collection_task_id)
            if not collection_task.completed:
                collection_task.delete()
                messages.success(request, 'Se ha eliminado correctamente.')
            else:
                messages.error(request, 'La tarea ya está completa y no puede eliminarse.')
            return redirect(reverse('collection_tasks', kwargs={'id': project_id}))
        return redirect('home')
    return redirect('index')

def modify_collection_task(request, project_id, collection_task_id):
    if System.is_logged(request):
        if System.is_admin(request):
           return render(request, 'rayuelaApp/collection_tasks/modify_collection_task.html', {'nav': 'block', 'project': Project.objects.get(id=project_id), 'collection_task': CollectionTask.objects.get(id=collection_task_id), 'sub_areas': ProjectSubArea.objects.filter(area=Project.objects.get(id=project_id).area)})
        return redirect('home')
    return redirect('index')

def process_modify_collection_task(request):
    if System.is_logged(request):
        if System.is_admin(request):
            request.session['project_id']=request.POST['project_id']
            request.session['collection_task_id'] = request.POST['collection_task_id']
            collection_task = CollectionTask.objects.get(id=request.session['collection_task_id'])
            collection_task.task_type = TaskType.objects.get(id=request.POST['select_task_types'])
            collection_task.time_restriction = TimeRestriction.objects.get(id=request.POST['select_time_restrictions'])
            collection_task.sub_area = ProjectSubArea.objects.get(id=request.POST['select_areas'])
            collection_task.save()
            messages.success(request, 'Se ha modificado correctamente')
            return redirect(reverse('collection_tasks', kwargs={'id': request.session['project_id']}))
        return redirect ('home')
    return redirect ('index')