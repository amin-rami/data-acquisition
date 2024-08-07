from django.db import models


class SensorData(models.Model):
    timestamp = models.DateTimeField()
    sensor_id = models.CharField(max_length=64)
    value = models.FloatField()
