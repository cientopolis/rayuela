from django.db import models
from rayuelaApp.models.project import Project
from rayuelaApp.models.user  import User
from datetime import datetime


class CheckIn(models.Model):

    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    project=models.ForeignKey(Project,on_delete=models.DO_NOTHING)
    latitude=models.CharField(blank=False,null=False,max_length=500)
    longitude=models.CharField(blank=False,null=False,max_length=500)
    datetime=models.DateTimeField(null=False, blank=False)
    

    class Meta:
        verbose_name='CheckIn'
        verbose_name_plural="CheckIns"
        db_table='check_in'

    def __str__(self):
        return f'{self.user},{self.project},{self.latitude},{self.longitude},{self.datetime}'


    def get_date(self):       
        return self.datetime
    
    def get_latitude(self):
        return self.latitude
    
    def get_longitude(self):
        return self.longitude
