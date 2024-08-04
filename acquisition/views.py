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
        if request.content_type == 'application/xml':
            data = Parser.xml_parser(data)
            data = data['root']['data']
        elif request.content_type == 'text/csv':
            data = Parser.csv_parser(data)
        elif request.content_type == 'text/yaml':
            data = Parser.yaml_parser(data)
        elif request.content_type == 'application/json':
            data = Parser.json_parser(data)

        serializer = SensorDataSerializer(data=data, many=(type(data) is list))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
