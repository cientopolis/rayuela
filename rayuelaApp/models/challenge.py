

from rayuelaApp.models.game_element import GameElement



class Challenge(GameElement):
   
    
    pass
    class Meta:
        verbose_name='Challenge'
        verbose_name_plural="Challenges"
        db_table='challenge'

    def __str__(self):
        return f'{self.name},{self.area},{self.time_restriction}'
 
    def is_valid_checkin(self,checkin_,user_id):
        return super().is_valid_checkin(checkin_,user_id)

    def update(self,name,area,time_restriction,goal):
       super().update(name,area,time_restriction,goal)
       self.save()

    