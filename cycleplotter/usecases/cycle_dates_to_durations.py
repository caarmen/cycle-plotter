import datetime as dt

from cycleplotter.entities.cycle_duration import CycleDuration


def cycle_dates_to_durations(cycle_dates: list[dt.datetime]):
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
