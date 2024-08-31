from django.db import models

class TaskType(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    description=models.CharField(max_length=250,blank=True,null=True)

    class Meta:
        verbose_name='Tipo de tarea'
        verbose_name_plural="Tipos de tarea"
        db_table='task_type'

    def __str__(self):
        return f'{self.name}'

    def create(self, name, description):
        task_type = self.create(name=name, description=description)
        return task_type

    def get_id(self):
        return self.id
