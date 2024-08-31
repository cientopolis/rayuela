from django.db import models

class Task(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    description=models.CharField(max_length=250,blank=True,null=True)

    class Meta:
        verbose_name='Tarea'
        verbose_name_plural="Tareas"
        db_table='task'

    def __str__(self):
        return f'{self.name}'

    def create(self, name, description):
        task = self.create(name=name, description=description)
        return task

    def get_id(self):
        return self.id
