import datetime as dt
import zipfile

from defusedxml import ElementTree as ET

from cycleplotter.model import CycleDuration
from cycleplotter.parser.base import Parser

DATE_FORMAT = "%Y-%m-%d %H:%M:%S %z"


class AppleHealthParser(Parser):
    def parse(self, input_data_path: str) -> list[CycleDuration]:
        xml_content = extract_xml_content(input_data_path)
        return parse_export(xml_content)


def extract_cycle_durations(cycle_dates: list[dt.datetime]):
    if len(cycle_dates) == 0:
        return []

    result = []

    current_cycle_date_start = cycle_dates[0]
    for i, cycle_date in enumerate(cycle_dates):
        delta_days_previous_log = (cycle_date - cycle_dates[i - 1]).days if i > 0 else 0
        if delta_days_previous_log > 3:
            result.append(
                CycleDuration(
                    start_date=current_cycle_date_start,
                    duration_days=(cycle_date - current_cycle_date_start).days,
                )
            )
            current_cycle_date_start = cycle_date

    return result


def parse_cycle_dates(xml_content: str) -> list[dt.datetime]:
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


def parse_export(xml_content: str) -> list[CycleDuration]:
    cycle_dates = parse_cycle_dates(xml_content)
    return extract_cycle_durations(cycle_dates)


def extract_xml_content(path: str) -> str:
    if path.endswith(".zip"):
        with zipfile.ZipFile(path, "r") as zip_ref:
            with zip_ref.open("apple_health_export/export.xml") as xml_file:
                return xml_file.read()
    with open(path) as xml_file:
        return xml_file.read()
