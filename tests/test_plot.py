from pathlib import Path

import pytest

from cycleplotter.usecases import extract_cycle_durations, plotter
from cycleplotter.usecases.parser.factory import Source


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
    fixture_path,
):
    image_output_path: Path = tmp_path / "test_output.png"
    assert not image_output_path.exists()
    cycle_durations = extract_cycle_durations(
        source, path=f"tests/fixtures/{source}/{fixture_path}.{extension}"
    )
    plotter.plot_cycle_durations(
        cycle_durations=cycle_durations,
        output_path=image_output_path,
    )
    assert image_output_path.exists()
