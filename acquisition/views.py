from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from acquisition.models import SensorData
from acquisition.serializers import SensorDataSerializer
from acquisition.utils import Parser


class SensorDataList(APIView):

    def get(self, request):
        serializer = SensorDataSerializer(SensorData.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.body.decode()
        data = Parser.parse(request.content_type, data)
        if data is None:
            return Response(data={"message": "unsupported content-type"}, status=status.HTTP_400_BAD_REQUEST)

        data = [data, ] if type(data) is dict else data
        serializer = SensorDataSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
