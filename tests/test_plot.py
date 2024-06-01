from pathlib import Path

import pytest

from cycleplotter import plotter
from cycleplotter.parser.factory import create_parser


@pytest.mark.parametrize(
    argnames=["fixture_path"],
    argvalues=[
        ("includes_other_data.xml",),
        ("beginning.xml",),
        ("end.xml",),
        ("pregnancy.xml",),
    ],
)
def test_plot_cycle_durations(
    tmp_path,
    fixture_path,
):
    image_output_path: Path = tmp_path / "test_output.png"
    assert not image_output_path.exists()
    parser = create_parser("applehealth")
    cycle_durations = parser.parse(input_data_path=f"tests/fixtures/{fixture_path}")
    plotter.plot_cycle_durations(
        cycle_durations=cycle_durations,
        output_path=image_output_path,
    )
    assert image_output_path.exists()
