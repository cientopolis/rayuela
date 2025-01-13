from django.db import models
# from rayuelaApp.models.task_type import TaskType
# from rayuelaApp.models.time_restriction import TimeRestriction
# from rayuelaApp.models.project_subarea import ProjectSubArea

class ScoreAllocationStrategy(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    points = models.IntegerField(blank=False, null=False, default=0)
    criterian_id = models.IntegerField(blank=False, null=False, default=0)

    class Meta:
        verbose_name='Estrategia de puntajes'
        verbose_name_plural="Estrategias de puntajes"
        db_table='score_allocation_strategy'

    def config(self, criterian_id, points):
        pass

    # def criterian_type(self):
    #     pass

class ScoreByCheckin(ScoreAllocationStrategy):
    class Meta:
        verbose_name='Puntuación por checkin'
        verbose_name_plural="Puntuaciones por checkin"
        db_table='score_by_checkin'

    def config(self, criterian_id, points):
        # En el caso de checkin, el contribution_id sera siempre 0 (cero)
        self.points = points
        self.criterian_id = criterian_id

    # def criterian_type(self):
    #     return "Checkin"

class ScoreByTaskType(ScoreAllocationStrategy):
    class Meta:
        verbose_name='Puntuación por tipo de tarea'
        verbose_name_plural="Puntuaciones por tipo de tarea"
        db_table='score_by_tasktype'

    def config(self, criterian_id, points):
        self.points = points
        self.criterian_id = criterian_id

    # def criterian_type(self):
    #     return "Tipo de tarea"

class ScoreByTimerRestriction(ScoreAllocationStrategy):
    class Meta:
        verbose_name='Puntuación por intervalo de tiempo'
        verbose_name_plural="Puntuaciones por intervalo de tiempo"
        db_table='score_by_timerestriction'

    def config(self, criterian_id, points):
        self.points = points
        self.criterian_id = criterian_id

    # def criterian_type(self):
    #     return "Intervalo de tiempo"

class ScoreByArea(ScoreAllocationStrategy):

    class Meta:
        verbose_name='Puntuación por área'
        verbose_name_plural="Puntuaciones por área"
        db_table='score_by_area'

    def config(self, criterian_id, points):
        self.points = points
        self.criterian_id = criterian_id

    # def criterian_type(self):
    #     return "Área"