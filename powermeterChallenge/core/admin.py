from django.contrib import admin

# Register your models here.
from core.models import Measurement, Meter


@admin.register(Meter)
class MeterAdmin(admin.ModelAdmin):
    list_display = ["id", "code", "name"]


@admin.register(Measurement)
class MeasuremenAdmin(admin.ModelAdmin):
    list_display = ["id", "meter_id", "timestamp", "consumption"]
