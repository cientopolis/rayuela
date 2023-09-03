
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from rayuelaApp.models.project import Project
import json


class GameElementView(TemplateView):
    template_name = 'create_challenge.html'

    @method_decorator(csrf_exempt)
   
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
    @csrf_exempt
    def post(self, request, *args, **kwargs):

        data = []
        data_time_restriction = []     
        data_area = []  
        data_subarea = []  
        try:
            action = request.POST['action']
            if action == 'search_time_restriction_id':
                project=Project.objects.get(id=int(request.POST['id']))      
                for i in project.time_restriction.all().order_by('id'):
                    data_time_restriction.append({'id': i.id, 'name': i.name})          
                data_area.append({'id': project.area.id, 'name': project.area.name})
                
                for subarea in project.area.projectsubarea_set.all():
                    data_subarea.append({'id': subarea.id,'number':subarea.number, 'subarea': json.loads(subarea.sub_area)['geometry']['coordinates'] })
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        data.append(data_time_restriction)
        data.append(data_area)
        data.append(data_subarea)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Aninados | Django'
        
        return context