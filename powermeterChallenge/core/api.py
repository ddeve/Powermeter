from django.db.models import Sum, Avg
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Meter, Measurement
from .serializers import MeterSerializer, MeasurementSerializer


class MeterViewSet(viewsets.ModelViewSet):
    queryset = Meter.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MeterSerializer

    @staticmethod
    def return_measurement(measurement: Measurement):
        serializer = MeasurementSerializer(measurement)
        if measurement:
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, name="Get Max Consumption")
    def get_max_consumption(self, request, pk=None):
        """Get the maximun comsumption of the meter"""
        measurement = (
            Measurement.objects.filter(meter__pk=pk).order_by("-consumption").first()
        )
        return self.return_measurement(measurement)

    @action(detail=True, name="Get Min Consumption")
    def get_min_consumption(self, request, pk=None):
        """Get the minimun comsumption of the meter"""
        measurement = (
            Measurement.objects.filter(meter__pk=pk).order_by("consumption").first()
        )
        return self.return_measurement(measurement)

    @action(detail=True, name="Get Total Consumption")
    def get_total_consumption(self, request, pk=None):
        """Get the total comsumption of the meter"""
        total_meter = Measurement.objects.filter(meter__pk=pk).aggregate(
            total_consumption=Sum("consumption")
        )
        total_meter["meter"] = pk
        return Response(total_meter)

    @action(detail=True, name="Get Average Consumption")
    def get_avg_consumption(self, request, pk=None):
        """Get the average comsumption of the meter"""
        avg_meter = Measurement.objects.filter(meter__pk=pk).aggregate(
            avg_consumption=Avg("consumption")
        )
        avg_meter["meter"] = pk
        return Response(avg_meter)


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MeasurementSerializer
