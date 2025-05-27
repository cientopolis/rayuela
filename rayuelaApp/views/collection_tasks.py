from django.shortcuts import redirect, reverse
from rayuelaApp.models.collection_task import CollectionTask
from rayuelaApp.models.project import Project
from rayuelaApp.utils.System import System
from django.contrib import messages

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