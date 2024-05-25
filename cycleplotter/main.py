import argparse
import dataclasses
import datetime as dt
import zipfile

import matplotlib.pyplot as plt
from defusedxml import ElementTree as ET

DATE_FORMAT = "%Y-%m-%d %H:%M:%S %z"


@dataclasses.dataclass
class CycleDuration:
    start_date: dt.datetime
    duration_days: int


def plot(input_data_path: str, output_path: str):
    xml_content = extract_xml_content(input_data_path)
    cycle_durations: list[CycleDuration] = parse_export(xml_content)
    plot_cycle_durations(cycle_durations=cycle_durations, output_path=output_path)


def extract_xml_content(path: str) -> str:
    if path.endswith(".zip"):
        with zipfile.ZipFile(path, "r") as zip_ref:
            with zip_ref.open("apple_health_export/export.xml") as xml_file:
                return xml_file.read()
    with open(path) as xml_file:
        return xml_file.read()


def parse_export(xml_content: str) -> list[CycleDuration]:
    cycle_dates = parse_cycle_dates(xml_content)
    return extract_cycle_durations(cycle_dates)


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


def plot_cycle_durations(
    cycle_durations: list[CycleDuration],
    output_path: str,
):
    start_dates = [cd.start_date for cd in cycle_durations]
    duration_days = [cd.duration_days for cd in cycle_durations]

    plt.figure(figsize=(11.69, 8.27))
    plt.scatter(start_dates, duration_days)
    plt.xlabel("Start date")
    plt.ylabel("Duration (days)")
    plt.title("Cycle Duration Over Time")
    plt.ylim(bottom=0, top=max(duration_days) * 1.05)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout(rect=[0.05, 0.05, 0.95, 0.95])
    plt.savefig(output_path)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file",
        help="path to export.xml file exported from Apple Health",
    )
    parser.add_argument(
        "output_file",
        help="path to image file to export",
    )
    args = parser.parse_args()
    plot(input_data_path=args.input_file, output_path=args.output_file)


if __name__ == "__main__":
    main()
