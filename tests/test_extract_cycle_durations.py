import datetime as dt

import pytest

from cycleplotter.entities.cycle_duration import CycleDuration
from cycleplotter.interfaceadapters.config import Source
from cycleplotter.interfaceadapters.cycledataparser.factory import (
    create_cycle_data_parser,
)
from cycleplotter.usecases import extract_cycle_durations


@pytest.mark.parametrize(
    argnames=["fixture_path", "expected_cycle_count"],
    argvalues=[
        ("includes_other_data", 6),
        ("beginning", 18),
        ("end", 15),
        ("pregnancy", 6),
    ],
)
def test_extract_cycle_durations(
    fixture_path: str,
    expected_cycle_count: int,
):

    cycle_durations_apple = extract_cycle_durations(
        create_cycle_data_parser(Source.APPLE),
        f"tests/fixtures/apple/{fixture_path}.xml",
    )
    cycle_durations_withings = extract_cycle_durations(
        create_cycle_data_parser(Source.WITHINGS),
        f"tests/fixtures/withings/{fixture_path}.csv",
    )

    assert len(cycle_durations_apple) == expected_cycle_count
    assert len(cycle_durations_withings) == expected_cycle_count

    # Convert to the same timezone to compare them:

    assert _convert_to_utc(cycle_durations_apple) == _convert_to_utc(
        cycle_durations_withings
    )


def _convert_to_utc(cycle_durations: list[CycleDuration]) -> list[CycleDuration]:
    return [
        CycleDuration(
            start_date=x.start_date.astimezone(dt.timezone.utc),
            duration_days=x.duration_days,
        )
        for x in cycle_durations
    ]
