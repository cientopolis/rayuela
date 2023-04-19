
from django.db import models
from alaapp.models.project_area import ProjectArea
from shapely.geometry import Point, Polygon
import json


class ProjectSubArea(models.Model):
    area=models.ForeignKey(ProjectArea,null=False,blank=False, on_delete=models.DO_NOTHING)
    sub_area=models.TextField(blank=False,null=False, max_length=800)
    number=models.IntegerField(blank=True,null=True)

    class Meta:
        verbose_name='ProjectSubArea'
        verbose_name_plural="ProjectSubAreas"
        db_table='project_subarea'

    def __str__(self):
        return f'{self.area},{self.sub_area}'  

    def is_valid_area(self,lat,lon):
        a=json.loads(self.sub_area)
        coords = []
        for coor in a['geometry']['coordinates'][0]:
            coords.append((coor[1],coor[0]))        
        p1 = Point(float(lat), float(lon) )   
        poly = Polygon(coords)   
        return p1.within(poly)

