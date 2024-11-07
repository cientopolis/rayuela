
from django.db import models
from rayuelaApp.models.badge_requirement import BadgeRequirement
from rayuelaApp.models.project import Project

class Badge(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.CharField(max_length=500, default='', blank=False, null=False)
    image = models.ImageField(upload_to='rayuelaApp/static/badge_image/', default='rayuelaApp/static/badge_image/badge.png', null=False, blank=False)
    requirements = models.ForeignKey(BadgeRequirement, related_name="Requerimientos", on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name='Badge'
        verbose_name_plural="Badges"
        db_table='badge'

    def __str__(self):
        return f'{self.name},{self.image}'

    def add_parent(self,id_parent):
        if id_parent !=0:
            self.parent=Badge.objects.get(id__exact=id_parent)
        else:
            self.parent=None

    def get_path_image(self):
        return self.image.path
    #
    # def can_add(self,user_id):
    #     if self.parent == None:
    #         return True
    #     return self.parent.get_assignment_set().filter(user_id=user_id).exists()
    #
    # def update(self,name,area,time_restriction,goal,id_parent):
    #    self.add_parent(id_parent)
    #    super().update(name,area,time_restriction,goal)
    #
    # def validate_badge(self,user_id):
    #     if self.parent == None:
    #         return True
    #     elif self.parent.get_progress_user(user_id)<100.0:
    #         return False
    #     return True
    
    
    
         
        
        

        
       
        