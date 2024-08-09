import xmltodict
import yaml
import json


class Parser:
    @staticmethod
    def parse(content_type, data):
        supported_types = [
            'application/json',
            'application/xml',
            'text/csv',
            'text/yaml',
        ]
        if content_type not in supported_types:
            return None
        if content_type == 'application/xml':
            parsed_data = Parser.xml_parser(data)
        elif content_type == 'text/csv':
            parsed_data = Parser.csv_parser(data)
        elif content_type == 'text/yaml':
            parsed_data = Parser.yaml_parser(data)
        elif content_type == 'application/json':
            parsed_data = Parser.json_parser(data)

        parsed_data = [parsed_data, ] if type(parsed_data) is dict else parsed_data
        return parsed_data

    @staticmethod
    def xml_parser(data):
        return xmltodict.parse(data)["root"]["data"]

    @staticmethod
    def csv_parser(data):
        lines = iter(data.splitlines())
        next(lines)

        parsed_data = []

        for line in lines:
            if line.strip() == "":
                continue
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
