from django.shortcuts import redirect, render
from alaapp.models.user import User
from alaapp.models.check_in import CheckIn
from alaapp.models.project import Project
from alaapp.utils.System import System
from django.contrib import messages



def checkin(request):
    if System.is_logged(request):
        if System.is_player(request):
            return render (request,'alaapp/checkin/create_checkin.html',{'nav':'block','create_checkin':System.get_navbar_color,'projects':User.objects.get(id__exact=request.session['id']).projects.all()})      
        redirect('home')
    return redirect('index')  

def process_checkin(request):
    if System.is_logged(request):
        if System.is_player(request):
            if not request.POST['datetime'] or not request.POST['lat'] or not request.POST['lon'] or not request.POST['project'] or request.POST['project']=='#':
                  messages.error(request,'Debe ingresar todos los campos')
            else:  
                checkin_=CheckIn(user=(User.objects.get(id__exact=request.session['id'])),project=(Project.objects.get(id__exact=request.POST['project'])),latitude=request.POST['lat'],longitude=request.POST['lon'],datetime=request.POST['datetime'])
                checkin_.save()                  
                project = Project.objects.get(id__exact=request.POST['project'])
                messages.success(request,'CheckIn realizado correctamente')
                project.add_checkin(checkin_,request)                          
            return checkin(request) 
        redirect('home')
    return redirect('index')  
