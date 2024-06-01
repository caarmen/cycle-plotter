import datetime as dt

from defusedxml import ElementTree as ET

from cycleplotter.infrastructure.files.reader import read_file
from cycleplotter.usecases.parser.base import BaseParser

DATE_FORMAT = "%Y-%m-%d %H:%M:%S %z"


class AppleHealthParser(BaseParser):
    def parse(self, input_data_path: str) -> list[dt.datetime]:
        xml_content = read_file(input_data_path, "apple_health_export/export.xml")

        document = ET.fromstring(xml_content)

        all_records = document.findall("Record")
        cycle_records = [
            record
            for record in all_records
            if record.get("type") == "HKCategoryTypeIdentifierMenstrualFlow"
            and record.get("value") != "HKCategoryValueMensturalFlowNone"
        ]
        start_dates_strs = [record.get("startDate") for record in cycle_records]
        start_dates = [
            dt.datetime.strptime(start_date_str, DATE_FORMAT)
            for start_date_str in start_dates_strs
        ]
        return start_dates
