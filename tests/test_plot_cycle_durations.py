from pathlib import Path

import pytest
from matplotlib import image as mpimage

from cycleplotter.interfaceadapters.cli.argparser import parse_size
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
@pytest.mark.parametrize(
    argnames=["input_size", "expected_width_px", "expected_height_px"],
    argvalues=[
        ("a4", 1169, 827),
        ("letter", 1100, 850),
        ("6x4in", 600, 400),
        ("600x400px", 600, 400),
        ("40x20cm", 1574, 787),
    ],
)
def test_plot_cycle_durations(
    tmp_path,
    source: Source,
    extension: str,
    duration_axis: DurationAxis,
    fixture_path,
    input_size: str,
    expected_width_px,
    expected_height_px,
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
            size=parse_size(input_size),
        ),
    )
    assert image_output_path.exists()
    img = mpimage.imread(image_output_path)
    actual_width_px = img.shape[1]
    actual_height_px = img.shape[0]
    assert actual_width_px == expected_width_px
    assert actual_height_px == expected_height_px
