import dataclasses
import enum


class DurationAxis(enum.StrEnum):
    X_AXIS = "x"
    Y_AXIS = "y"
    BOTH = "both"


@dataclasses.dataclass
class PlotConfig:
    duration_axis: DurationAxis = DurationAxis.BOTH
