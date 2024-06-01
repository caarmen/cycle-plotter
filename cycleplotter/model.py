import dataclasses
import datetime as dt


@dataclasses.dataclass
class CycleDuration:
    start_date: dt.datetime
    duration_days: int
