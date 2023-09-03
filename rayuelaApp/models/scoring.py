
from django.db import models
from rayuelaApp.models.criteria import Criteria
from rayuelaApp.models.assignment import Assignment


class Scoring(models.Model):
    assignment=models.ForeignKey(Assignment,blank=False,null=False,on_delete=models.DO_NOTHING)
    criteria= models.ForeignKey(Criteria,blank=False,null=False,on_delete=models.DO_NOTHING)
    assessment=models.IntegerField(blank=True,null=True)

    class Meta:
        verbose_name='Scoring'
        verbose_name_plural="Scorings"
        db_table='scoring'

 

    def __str__(self):
        return f'{self.assignment},{self.criteria},{self.assessment}'     

    
