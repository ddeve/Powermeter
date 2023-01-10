from rest_framework import serializers

from .models import Measurement, Meter


class MeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meter
        fields = ("id", "code", "name")


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ("id", "meter", "timestamp", "consumption")
