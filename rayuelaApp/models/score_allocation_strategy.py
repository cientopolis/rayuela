from django.db import models
from rayuelaApp.models.task_type import TaskType
from rayuelaApp.models.time_restriction import TimeRestriction
from rayuelaApp.models.project_subarea import ProjectSubArea
from rayuelaApp.models.project import Project

class ScoreAllocationStrategy(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    points = models.IntegerField(blank=False, null=False, default=0)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    checkin = models.BooleanField(default=False, blank=True, null=True)
    task_type = models.ForeignKey(TaskType, on_delete=models.DO_NOTHING, blank=True, null=True)
    time_restriction = models.ForeignKey(TimeRestriction, on_delete=models.DO_NOTHING, blank=True, null=True)
    sub_area = models.ForeignKey(ProjectSubArea, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name='Estrategia de puntajes'
        verbose_name_plural="Estrategias de puntajes"
        db_table='score_allocation_strategy'
