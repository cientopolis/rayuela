
from django.db import models
from rayuelaApp.models.game_element import GameElement

class Badge(GameElement):
    image=models.ImageField(upload_to='rayuelaApp/static/game_elements_image/',default='rayuelaApp/static/game_elements_image/ge.jpg',null=False,blank=False)
    parent=models.ForeignKey('self',null=True,blank=True,on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name='Badge'
        verbose_name_plural="Badges"
        db_table='badge'

    def __str__(self):
        return f'{self.image},{self.parent}'

    def is_valid_checkin(self,checkin_,user_id):       
        return (self.validate_badge(user_id) and super().is_valid_checkin(checkin_,user_id))
    
    def add_parent(self,id_parent):
        if id_parent !=0:
            self.parent=Badge.objects.get(id__exact=id_parent)
        else:
            self.parent=None

    def get_path_image(self):       
        return self.image.path
    
    def can_add(self,user_id):
        if self.parent == None:
            return True
        return self.parent.get_assignment_set().filter(user_id=user_id).exists()

    def update(self,name,area,time_restriction,goal,id_parent):
       self.add_parent(id_parent)
       super().update(name,area,time_restriction,goal)

    def validate_badge(self,user_id):
        if self.parent == None:
            return True
        elif self.parent.get_progress_user(user_id)<100.0:    
            return False
        return True
    
    
    
         
        
        

        
       
        