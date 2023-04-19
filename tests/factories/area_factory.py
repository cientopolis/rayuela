import factory

from alaapp.models.project_area import ProjectArea
from alaapp.models.project_subarea import ProjectSubArea

class ProjectAreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectArea
    
    name='test_area'

class ProjectSubAreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectSubArea
    
    area=factory.SubFactory(ProjectAreaFactory)
    sub_area='{"id": "0", "type": "Feature", "properties": {"Ciudad": "La Plata", "AreaAInterceptar": "Bosque de la Plata"}, "geometry": {"type": "Polygon", "coordinates": [[[-57.9414, -34.9119], [-57.9276, -34.9119], [-57.9276, -34.9062], [-57.9414, -34.9062], [-57.9414, -34.9119]]]}}'  
    number=1

class OtherProjectSubAreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectSubArea
    
    area=factory.SubFactory(ProjectAreaFactory)
    sub_area='{"id": "0", "type": "Feature", "properties": {"Ciudad": "La Plata", "AreaAInterceptar": "Bosque de la Plata"}, "geometry": {"type": "Polygon", "coordinates": [[[-57.9414, -34.9119], [-57.9276, -34.9119], [-57.9276, -34.9062], [-57.9414, -34.9062], [-57.9414, -34.9119]]]}}'  
    number=2