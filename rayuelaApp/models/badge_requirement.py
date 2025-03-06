from django.db import models
from rayuelaApp.models.task_type import TaskType
from rayuelaApp.models.time_restriction import TimeRestriction
from rayuelaApp.models.project_subarea import ProjectSubArea

class BadgeRequirement(models.Model):
    task_type = models.ForeignKey(TaskType, on_delete=models.DO_NOTHING, blank=True, null=True)
    time_restriction = models.ForeignKey(TimeRestriction, on_delete=models.DO_NOTHING, blank=True, null=True)
    sub_area = models.ForeignKey(ProjectSubArea, on_delete=models.DO_NOTHING, blank=True, null=True)
    times = models.IntegerField(blank=False, null=False, default=0)
    badge_id = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return f'{self.task_type},{self.times},{self.badge_id}'
    
    class Meta:
        verbose_name='Requerimiento'
        verbose_name_plural="Requerimientos"
        db_table='badge_requirement'
