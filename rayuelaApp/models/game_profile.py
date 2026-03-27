from django.db import models
from rayuelaApp.models.badge import Badge
from rayuelaApp.models.project import Project
from users.models import Volunteer


class Participation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    points = models.IntegerField(blank=False, null=False, default=0)
    badge = models.ForeignKey(Badge, blank=True, null=True, on_delete=models.DO_NOTHING)


class GameProfile(models.Model):
    user = models.ForeignKey(Volunteer, on_delete=models.DO_NOTHING)
    participations = models.ManyToManyField(Participation)

    def set_participation(self, project, points, badge=None):
        participation = Participation.objects.create(project=project, points=points, badge=badge)
        self.participations.add(participation)
