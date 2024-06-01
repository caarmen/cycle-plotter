import datetime as dt

from cycleplotter.entities.cycle_duration import CycleDuration
from cycleplotter.usecases import cycle_dates_to_durations
from cycleplotter.usecases.parser.base import Parser


def extract_cycle_durations(parser: Parser, path: str) -> list[CycleDuration]:
    cycle_datetimes: list[dt.datetime] = parser.parse(input_data_path=path)
    return cycle_dates_to_durations(cycle_datetimes)
