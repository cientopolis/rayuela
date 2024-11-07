from django.db import models
from rayuelaApp.models.task_type import TaskType

class BadgeRequirement(models.Model):
    #name = models.CharField(max_length=30)
    task_type = models.ForeignKey(TaskType, on_delete=models.DO_NOTHING)
    times = models.IntegerField(blank=False, null=False, default=0)
    badge_id = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return f'{self.task_type},{self.times},{self.badge_id}'
    
    class Meta:
        verbose_name='Requerimiento'
        verbose_name_plural="Requerimientos"
        db_table='badge_requirement'
