
from django.db import models

from rayuelaApp.models.game_profile import GameProfile
from rayuelaApp.models.project import Project

class Leaderboard(models.Model):
    order_by_points = models.BooleanField(default=True)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name='Tabla de posiciones'
        verbose_name_plural="Tablas de posiciones"
        db_table='leaderboard'

class Competition(models.Model):
    game_profile = models.ForeignKey(GameProfile, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    total_points = models.IntegerField(blank=False, null=False, default=0)
    total_badges = models.IntegerField(blank=False, null=False, default=0)

    def update_total_points(self, points):
        self.total_points = self.total_points + points

    def update_total_badges(self, badge):
        self.total_badges = self.total_badges + badge