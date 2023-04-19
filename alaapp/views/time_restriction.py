from django.shortcuts import redirect, render
from alaapp.models.time_restriction import TimeRestriction
from alaapp.models.day import Day
from alaapp.models.project import Project
from alaapp.utils.System import System
from django.contrib import messages




def time_restriction(request):
    if System.is_logged(request):
        if System.is_admin(request):

             
             if request.method == 'POST':
                return render(request, 'alaapp/time_restriction/create_time_restriction.html',{'nav':'block','create_time_restriction':System.get_navbar_color, 'days':Day.objects.all(), 'project': Project.objects.get(id=request.POST['project_id'])})
             else:
                return render(request, 'alaapp/time_restriction/create_time_restriction.html',{'nav':'block','create_time_restriction':System.get_navbar_color, 'days':Day.objects.all(), 'project': Project.objects.get(id=request.session['project_id'])})
        return redirect ('home')
    return redirect ('index')

def process_time_restriction(request):
    if System.is_logged(request):
        if System.is_admin(request): 
            request.session['project_id']=request.POST['project_id']
            if not request.POST['name']:
                messages.error(request,'Debe seleccionar un nombre')
                return redirect ('create_time_restriction')
            if not request.POST.get('1') and not request.POST.get('2') and  not request.POST.get('3') and  not request.POST.get('4') and  not request.POST.get('5') and  not request.POST.get('6') and  not request.POST.get('7'):
                messages.error(request,'Debe seleccionar al menos un día')
                return redirect ('create_time_restriction')           
            datetimes=request.POST['datetime'].split(' ')           
            tr=TimeRestriction(name=request.POST['name'],date_from=datetimes[0], date_to=datetimes[3])       
            tr.add_hours(request.POST.get('hour'),datetimes[1],datetimes[4])        
            tr.add_days(request.POST)
            Project.objects.get(id=request.POST['project_id']).add_time_restriction(tr.get_id())
            return redirect ('modify_project')
        return redirect ('home')
    return redirect ('index')