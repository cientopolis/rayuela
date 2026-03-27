from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Valuation(models.Model):
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #TODO: revisar decimales
    comment = models.CharField(max_length=400, blank=False, null=False)