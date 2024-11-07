from django.shortcuts import redirect, render, reverse
from rayuelaApp.models.project import Project
from rayuelaApp.models.task_type import TaskType
from rayuelaApp.utils.System import System
from django.contrib import messages

def automatic_task_generation(request, id):
    if System.is_logged(request):
        if System.is_admin(request):
            if request.method == 'POST':
                project = Project.objects.get(id=id)
                project.automatic_task_generation()
                return redirect(reverse('collection_tasks', kwargs={'id': id}))
            # else:
            #     return render(request, 'rayuelaApp/task/create_task_type.html',
            #                   {'nav': 'block', 'create_task_type': System.get_navbar_color,
            #                    'project': Project.objects.get(id=id)})
        return redirect ('home')
    return redirect ('index')