from django.db import models


class Criteria(models.Model):
    name=models.CharField(max_length=500,blank=False,null=False)
  

    class Meta:
        verbose_name='Criteria'
        verbose_name_plural="Criterias"
        db_table='criteria'



    def __str__(self):
        return f'{self.name}' 

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id    
