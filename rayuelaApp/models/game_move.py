from django.db import models

from rayuelaApp.models.badge import Badge
from rayuelaApp.models.check_in import CheckIn
from rayuelaApp.models.collection_task import CollectionTask
from rayuelaApp.models.game_profile import GameProfile
from rayuelaApp.models.valuation import Valuation


class GameMove(models.Model):
    points = models.IntegerField(blank=True, null=True, default=0)
    checkin = models.ForeignKey(CheckIn, blank=True, null=True, on_delete=models.DO_NOTHING)
    game_profile = models.ForeignKey(GameProfile, blank=True, null=True, on_delete=models.DO_NOTHING)
    badge = models.ForeignKey(Badge, blank=True, null=True, on_delete=models.DO_NOTHING)
    collection_task = models.ForeignKey(CollectionTask, blank=True, null=True, on_delete=models.DO_NOTHING)
    valuation = models.ForeignKey(Valuation, blank=True, null=True, on_delete=models.DO_NOTHING)
