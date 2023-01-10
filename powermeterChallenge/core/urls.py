from rest_framework import routers

from .api import MeterViewSet, MeasurementViewSet

router = routers.DefaultRouter()

router.register("api/meter", MeterViewSet, "meter")
router.register("api/measurement", MeasurementViewSet, "measurement")

urlpatterns = router.urls
