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

        DATETIME_INDEX = 0
        parsed_data = []

        for line in lines:
            values = line.split(',')
            timestamp = values[DATETIME_INDEX]
            del values[DATETIME_INDEX]
            value = ','.join(values)
            row = {"timestamp": timestamp, "value": value}
            parsed_data.append(row)
        return parsed_data

    @staticmethod
    def yaml_parser(data):
        return yaml.safe_load(data)

    @staticmethod
    def json_parser(data):
        return json.loads(data)
