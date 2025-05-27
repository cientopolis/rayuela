from django.db import models

from rayuelaApp.models.project_subarea import ProjectSubArea
from rayuelaApp.models.task_type import TaskType
from rayuelaApp.models.project_area import ProjectArea
from rayuelaApp.models.time_restriction import TimeRestriction

class CollectionTask(models.Model):
    task_type = models.ForeignKey(TaskType, related_name="tipo_de_tarea", on_delete=models.DO_NOTHING)
    sub_area = models.ForeignKey(ProjectSubArea, on_delete=models.DO_NOTHING)
    time_restriction = models.ForeignKey(TimeRestriction, on_delete=models.DO_NOTHING)
    completed = models.BooleanField(default=False, blank=False, null=False)

    class Meta:
        verbose_name='Tarea de recolección'
        verbose_name_plural="Tareas de recolección"
        db_table = 'collection_task'
