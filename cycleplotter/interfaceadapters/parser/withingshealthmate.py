import csv
import datetime as dt

from cycleplotter.infrastructure.files.opener import open_file
from cycleplotter.usecases.parser.base import Parser

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class WithingsHealthmateParser(Parser):
    def parse(self, input_data_path: str) -> list[dt.datetime]:
        with open_file(input_data_path, "other.csv") as file:
            reader = csv.DictReader(file)
            return [
                dt.datetime.strptime(row["date"], DATE_FORMAT).replace(
                    tzinfo=dt.timezone.utc
                )
                for row in reader
                if row["type"] == "Menstruation flow"
            ]
