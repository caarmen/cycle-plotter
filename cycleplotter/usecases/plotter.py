import matplotlib.pyplot as plt

from cycleplotter.entities.cycle_duration import CycleDuration


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
