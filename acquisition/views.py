from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from acquisition.models import SensorData
from acquisition.serializers import SensorDataSerializer
from acquisition.utils import Parser
from acquisition.dependencies import MessageBrokerType, get_message_broker
from datagateway.settings import SENSORDATA_TOPIC


class SensorDataList(APIView):

    def get(self, request):
        serializer = SensorDataSerializer(SensorData.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.body.decode()
        data = Parser.parse(request.content_type, data)
        if data is None:
            return Response(data={"message": "unsupported content-type"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = SensorDataSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        message_broker = get_message_broker(MessageBrokerType.KAFKA)
        message_broker.send(serializer.data, SENSORDATA_TOPIC)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
