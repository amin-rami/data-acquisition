from django.urls import path
from acquisition.views import SensorDataList


urlpatterns = [
    path('sensordata/', SensorDataList.as_view())
]
