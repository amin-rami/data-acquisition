from django.db import models



class SensorData(models.Model):
    timestamp = models.DateTimeField()
    value = models.CharField(max_length=2048)
