from rest_framework import serializers
from acquisition.models import SensorData


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        exclude = ('id', )
