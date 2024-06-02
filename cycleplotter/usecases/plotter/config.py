import dataclasses
import enum


class DurationAxis(enum.StrEnum):
    X_AXIS = "x"
    Y_AXIS = "y"
    BOTH = "both"


@dataclasses.dataclass
class Size:
    width_inches: float
    height_inches: float


SIZE_LETTER = Size(
    width_inches=11,
    height_inches=8.5,
)

SIZE_A4 = Size(
    width_inches=11.69,
    height_inches=8.27,
)


@dataclasses.dataclass
class PlotConfig:
    duration_axis: DurationAxis = DurationAxis.BOTH
    size: Size = dataclasses.field(default_factory=lambda: SIZE_A4)
