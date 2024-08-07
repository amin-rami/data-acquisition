import xmltodict
import yaml
import json


class Parser:
    @staticmethod
    def xml_parser(data):
        return xmltodict.parse(data)

    @staticmethod
    def csv_parser(data):
        lines = iter(data.splitlines())
        next(lines)

        parsed_data = []

        for line in lines:
            items = line.split(',')
            items = [x.strip() for x in items]
            timestamp, sensor_id, value = items
            row = {"timestamp": timestamp, "sensor_id": sensor_id, "value": value}
            parsed_data.append(row)
        return parsed_data

    @staticmethod
    def yaml_parser(data):
        return yaml.safe_load(data)

    @staticmethod
    def json_parser(data):
        return json.loads(data)
