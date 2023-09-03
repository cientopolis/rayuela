
from django.db import models

import json


class ProjectArea(models.Model):
    name=models.CharField(blank=False,null=False,max_length=200)
    
    class Meta:
        verbose_name='ProjectArea'
        verbose_name_plural="ProjectAreas"
        db_table='project_area'

    def __str__(self):
        return f'{self.name}'  
   

    def add_subareas(self,areas):
        from rayuelaApp.models.project_subarea import ProjectSubArea
        i=1
        for subarea in areas:
            p_subarea=ProjectSubArea(area=self,sub_area=json.dumps(subarea),number=i)
            p_subarea.save()
            i=i+1  
        self.save()  