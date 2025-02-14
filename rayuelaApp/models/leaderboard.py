
from django.db import models
from rayuelaApp.models.project import Project

class Leaderboard(models.Model):
    order_by_points = models.BooleanField(blank=False, null=False, default=True)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name='Tabla de posiciones'
        verbose_name_plural="Tablas de posiciones"
        db_table='leaderboard'
