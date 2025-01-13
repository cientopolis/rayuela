from django.db import models
from rayuelaApp.models.project import Project
from rayuelaApp.models.score_allocation_strategy import ScoreAllocationStrategy

class Score(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    scores = models.ManyToManyField(ScoreAllocationStrategy, blank=True)

    class Meta:
        verbose_name='Puntuación de juego'
        verbose_name_plural="Puntuaciones del juego"
        db_table='game_scores'

    def __str__(self):
        return f'{self.project}'

    def add_score(self, score):
        self.scores.add(score)
        self.save()