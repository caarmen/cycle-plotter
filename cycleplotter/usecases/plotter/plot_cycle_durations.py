import datetime as dt

import matplotlib.pyplot as plt

from cycleplotter.entities.cycle_duration import CycleDuration
from cycleplotter.usecases.plotter.config import (
    SIZE_A4,
    SIZE_LETTER,
    DurationAxis,
    PlotConfig,
)

DATE_FORMAT = "%Y-%m-%d"


def plot_cycle_durations(
    config: PlotConfig,
    cycle_durations: list[CycleDuration],
    output_path: str,
):

    plt.figure(figsize=(config.size.width_inches, config.size.height_inches))
    plt.title("Cycle Duration Over Time")

    x_axis_values = _get_x_axis_values(cycle_durations, config.duration_axis)
    y_axis_values = _get_y_axis_values(cycle_durations, config.duration_axis)
    plt.scatter(x_axis_values, y_axis_values)
    plt.xlabel("Start date")

    # Configuration for if we want to show the cycle duration on the y-axis:
    if config.duration_axis in (DurationAxis.Y_AXIS, DurationAxis.BOTH):
        # Force some vertical padding in days.
        # This prevents a graph from looking like there's huge variations in
        # data when the data is very regular (low stdev).
        max_duration_days = max(y_axis_values)
        min_duration_days = min(y_axis_values)
        vertical_padding_days = max(5, (max_duration_days - min_duration_days) * 0.1)
        plt.ylabel("Duration (days)")
        plt.ylim(
            bottom=min_duration_days - vertical_padding_days,
            top=max_duration_days + vertical_padding_days,
        )
    # If we ONLY want to indicate duration on the y-axis, by default we'd have
    # one x-axis label per point. This is because our x-axis labels are strings, not
    # datestimes, and matplotlib only knows how to intelligently space datetimes.
    # This can be crowded. Configure the x-axis labels so that we have at most
    # 10 labels total in the graph.
    if config.duration_axis == DurationAxis.Y_AXIS:
        point_count = len(x_axis_values)
        if point_count > 10:
            interval = point_count // 10
            plt.xticks(
                ticks=x_axis_values[::interval],
                labels=x_axis_values[::interval],
            )
    # If we ONLY want to indicate duration on the x-axis, remove all labels on the y-axis.
    if config.duration_axis == DurationAxis.X_AXIS:
        plt.yticks(ticks=[])

    plt.grid(True)

    plt.xticks(rotation=45)
    # If the size is letter or a4, assume it's for printing, and include margins:
    if config.size in (SIZE_LETTER, SIZE_A4):
        plt.tight_layout(rect=[0.05, 0.05, 0.95, 0.95])
    else:
        plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def _get_x_axis_values(
    cycle_durations: list[CycleDuration],
    duration_axis: DurationAxis,
) -> list[dt.datetime | str]:
    """
    :return: a list of datetime of the cycle start dates,
        if duration_axis includes tye x-axis,
        a list of string representations of the cycle start dates otherwise.
    """
    if duration_axis in (DurationAxis.X_AXIS, DurationAxis.BOTH):
        return [cd.start_date for cd in cycle_durations]
    return [cd.start_date.strftime(DATE_FORMAT) for cd in cycle_durations]


def _get_y_axis_values(
    cycle_durations: list[CycleDuration],
    duration_axis: DurationAxis,
) -> list[int]:
    """
    :return: a list of cycle durations if duration_axis includes the y-axis,
        a list of the number 1 otherwise.
    """

    if duration_axis in (DurationAxis.Y_AXIS, DurationAxis.BOTH):
        return [cd.duration_days for cd in cycle_durations]
    return [1 for _ in cycle_durations]
