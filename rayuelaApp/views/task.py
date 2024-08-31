from django.shortcuts import redirect, render
from rayuelaApp.models.project import Project
from rayuelaApp.models.task import Task
from rayuelaApp.utils.System import System
from django.contrib import messages

def task(request, project_id):
    if System.is_logged(request):
        if System.is_admin(request):
             if request.method == 'POST':
                return render(request, 'rayuelaApp/task/create_task.html',{'nav':'block','create_task':System.get_navbar_color, 'project': Project.objects.get(id=project_id)})
             else:
                return render(request, 'rayuelaApp/task/create_task.html',{'nav':'block','create_task':System.get_navbar_color, 'project': Project.objects.get(id=project_id)})
        return redirect ('home')
    return redirect ('index')

def process_task(request):
    if System.is_logged(request):
        if System.is_admin(request):
            request.session['project_id']=request.POST['project_id']
            if not request.POST['name']:
                messages.error(request,'Debe seleccionar un nombre')
                return redirect ('create_task')
            task = Task.objects.create(name=request.POST['name'], description=request.POST['description'])
            Project.objects.get(id=request.POST['project_id']).add_task(task.get_id())
            return redirect ('modify_project')
        return redirect ('home')
    return redirect ('index')