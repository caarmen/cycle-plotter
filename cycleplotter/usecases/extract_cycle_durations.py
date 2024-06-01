import datetime as dt

from cycleplotter.entities.cycle_duration import CycleDuration
from cycleplotter.usecases import cycle_dates_to_durations
from cycleplotter.usecases.parser.factory import Parser, create_parser


def extract_cycle_durations(parser: Parser, path: str) -> list[CycleDuration]:
    parser_instance = create_parser(parser)
    cycle_datetimes: list[dt.datetime] = parser_instance.parse(input_data_path=path)
    return cycle_dates_to_durations(cycle_datetimes)
