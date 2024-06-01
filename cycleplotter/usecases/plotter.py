import matplotlib.pyplot as plt

from cycleplotter.entities.cycle_duration import CycleDuration


def plot_cycle_durations(
    cycle_durations: list[CycleDuration],
    output_path: str,
):
    start_dates = [cd.start_date for cd in cycle_durations]
    duration_days = [cd.duration_days for cd in cycle_durations]

    # Force some vertical padding in days.
    # This prevents a graph from looking like there's huge variations in
    # data when the data is very regular (low stdev).
    max_duration_days = max(duration_days)
    min_duration_days = min(duration_days)
    vertical_padding_days = max(5, (max_duration_days - min_duration_days) * 0.1)

    plt.figure(figsize=(11.69, 8.27))
    plt.scatter(start_dates, duration_days)
    plt.xlabel("Start date")
    plt.ylabel("Duration (days)")
    plt.title("Cycle Duration Over Time")
    plt.ylim(
        bottom=min_duration_days - vertical_padding_days,
        top=max_duration_days + vertical_padding_days,
    )
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout(rect=[0.05, 0.05, 0.95, 0.95])
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.savefig(output_path)
