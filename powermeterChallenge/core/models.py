from django.db import models
from django.core.validators import MinValueValidator


class Meter(models.Model):
    code = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)


class Measurement(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.PROTECT)
    timestamp = models.DateTimeField()
    consumption = models.DecimalField(
        decimal_places=2, max_digits=16, validators=[MinValueValidator(0)]
    )
