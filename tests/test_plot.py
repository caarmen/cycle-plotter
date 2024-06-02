from pathlib import Path

import pytest

from cycleplotter.interfaceadapters.config import Source
from cycleplotter.interfaceadapters.cycledataparser.factory import (
    create_cycle_data_parser,
)
from cycleplotter.usecases import extract_cycle_durations
from cycleplotter.usecases.plotter import DurationAxis, PlotConfig, plot_cycle_durations


@pytest.mark.parametrize(
    argnames=["duration_axis"],
    argvalues=[
        (DurationAxis.X_AXIS,),
        (DurationAxis.Y_AXIS,),
        (DurationAxis.BOTH,),
    ],
)
@pytest.mark.parametrize(
    argnames=["source", "extension"],
    argvalues=[
        (Source.APPLE, "xml"),
        (Source.WITHINGS, "csv"),
    ],
)
@pytest.mark.parametrize(
    argnames=["fixture_path"],
    argvalues=[
        ("includes_other_data",),
        ("beginning",),
        ("end",),
        ("pregnancy",),
    ],
)
def test_plot_cycle_durations(
    tmp_path,
    source: Source,
    extension: str,
    duration_axis: DurationAxis,
    fixture_path,
):
    image_output_path: Path = tmp_path / "test_output.png"
    assert not image_output_path.exists()
    cycle_durations = extract_cycle_durations(
        create_cycle_data_parser(source),
        path=f"tests/fixtures/{source}/{fixture_path}.{extension}",
    )
    plot_cycle_durations(
        cycle_durations=cycle_durations,
        output_path=image_output_path,
        config=PlotConfig(
            duration_axis=duration_axis,
        ),
    )
    assert image_output_path.exists()
