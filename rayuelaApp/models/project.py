
from django.db import models
from django.contrib import messages
from rayuelaApp.models.project_area  import ProjectArea
from rayuelaApp.models.time_restriction  import TimeRestriction
from rayuelaApp.models.user import User


class Project(models.Model):
    name=models.CharField(max_length=30,blank=False,null=False)
    description=models.CharField(max_length=500,blank=True,null=True)
    image=models.ImageField(upload_to='rayuelaApp/static/project_image/',default='rayuelaApp/static/project_image/rio.jpg',null=False,blank=False)
    web=models.CharField(max_length=100,blank=True,null=True)
    available=models.BooleanField(default=False, blank=False, null=False)
    admins=models.ManyToManyField(User, related_name='admins')
    area=models.ForeignKey(ProjectArea,blank=True,null=True,on_delete=models.DO_NOTHING)
    time_restriction=models.ManyToManyField(TimeRestriction)
    

    def __str__(self):
        return f'{self.name},{self.description},{self.web},{self.image},{self.admins},{self.area},{self.time_restriction}'

    class Meta:
        verbose_name='Project'
        verbose_name_plural="Projects"
        db_table='project'

    def add_checkin(self,checkin_,request): 
        from rayuelaApp.models.game_element import GameElement
        s_gr=''
        for ge in self.get_game_elements():     
            g=GameElement.objects.get_subclass(id=ge.get_id())             
            if g.is_valid_checkin(checkin_,request.session['id']):     
                g.add_checkin(checkin_)
                g.increment_progress(request.session['id'])          
                s_gr= s_gr + g.get_name() + '<br/>'
        messages.success(request,'Progreso actualizado en los Elementos de juego: %s'  % (s_gr))                
        self.save()

    def add_admins(self,id_admins):
        for id_admin in id_admins:
            self.admins.add(User.objects.get(id=id_admin))
        self.save()

    def add_area(self,area):
        self.area=area
        self.save()

    def modify(self,name,description,web,checkbox):
        self.name=name
        self.description=description
        self.web=web
        if (checkbox == 'on'):
            self.available=1
        else:
            self.available=0
        
    def add_time_restrictions(self,id_time_restrictions):
        self.time_restriction.clear()   
        for id_tr in id_time_restrictions:
            self.add_time_restriction(id_tr)
        self.save()


    def add_time_restriction(self,id_time_restriction):       
        self.time_restriction.add(TimeRestriction.objects.get(id=id_time_restriction))
        self.save()

    def get_game_elements(self):
        return self.gameelement.all()

    def set_name(self,name_):
        self.name=name_
        self.save()

    def get_name(self):
        return self.name

    def get_image_path(self):
        return self.image.path

    def get_id(self):
        return self.id

    def get_area(self):
        return self.area

    def add_admin(self,admin):
        self.admins.add(admin)

    def add_time_restriction(self,time_restriction):
        self.time_restriction.add(time_restriction)

    def is_my_admin(self,admin_id):     
        return self.admins.filter(id=admin_id).exists()

    def update_admins(self,id_admins):
        self.admins.clear()
        self.add_admins(id_admins)
        self.save()
    
    def is_my_time_restriction(self,time_restriction_id):
        return self.time_restriction.filter(id=time_restriction_id).exists()
        
    def set_available(self,available_):
        self.available=available_
        self.save()

    def get_available(self):
        return self.available
    
    def get_time_restrictions(self):
        return self.time_restriction