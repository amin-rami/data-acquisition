from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from acquisition.models import SensorData
from acquisition.serializers import SensorDataSerializer


class SensorDataList(APIView):

    def get(self, request):
        serializer = SensorDataSerializer(SensorData.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SensorDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
