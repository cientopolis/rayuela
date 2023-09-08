
from django.db import models
from rayuelaApp.models.user import User
from rayuelaApp.models.game_element import GameElement





class Assignment(models.Model):
    user= models.ForeignKey(User,blank=False,null=False,on_delete=models.DO_NOTHING)
    progress=models.FloatField(default=0,blank=False,null=False)
    game_element=models.ForeignKey(GameElement,blank=False,null=False,on_delete=models.DO_NOTHING)
    like_dislike=models.BooleanField(blank=True,null=True)

    class Meta:
        verbose_name='Assignment'
        verbose_name_plural="Assignment"
        db_table='assignment'



    def __str__(self):
        return f'{self.user},{self.progress}'     

    
    def increment_progress(self,goal,count):
        if (self.progress<100):
            self.progress=(count / goal)*100    
            self.save()

    def get_like_dislike(self):
        return self.like_dislike
    
    def add_like_dislike(self,bool):
        if bool == 'true':
            self.like_dislike=True
        else:
            self.like_dislike=False
        self.save()

    def add_scorings(self,assesments):
        from rayuelaApp.models.criteria import Criteria
        from rayuelaApp.models.scoring import Scoring
        for criteria in Criteria.objects.all():
            Scoring(assessment=assesments[criteria.get_name()],criteria=criteria,assignment=self).save()     

    def get_id(self):
        return self.id

    def get_progress(self):
        return self.progress