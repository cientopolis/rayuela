from django.db import models


class Day(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
  

    class Meta:
        verbose_name='Day'
        verbose_name_plural="Days"
        db_table='day'



    def __str__(self):
        return f'{self.name}' 

    def get_id(self):
        return str(self.id)

    