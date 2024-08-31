from django.shortcuts import redirect, render
from rayuelaApp.models.project import Project
from rayuelaApp.models.task_type import TaskType
from rayuelaApp.utils.System import System
from django.contrib import messages

def task_type(request, project_id):
    if System.is_logged(request):
        if System.is_admin(request):
             if request.method == 'POST':
                return render(request, 'rayuelaApp/task/create_task_type.html',{'nav':'block','create_task_type':System.get_navbar_color, 'project': Project.objects.get(id=project_id)})
             else:
                return render(request, 'rayuelaApp/task/create_task_type.html',{'nav':'block','create_task_type':System.get_navbar_color, 'project': Project.objects.get(id=project_id)})
        return redirect ('home')
    return redirect ('index')

def process_task_type(request):
    if System.is_logged(request):
        if System.is_admin(request):
            request.session['project_id']=request.POST['project_id']
            if not request.POST['name']:
                messages.error(request,'Debe seleccionar un nombre')
                return redirect ('create_task_type')
            task_type = TaskType.objects.create(name=request.POST['name'], description=request.POST['description'])
            Project.objects.get(id=request.POST['project_id']).add_task_type(task_type.get_id())
            return redirect ('modify_project')
        return redirect ('home')
    return redirect ('index')