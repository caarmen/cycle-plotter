from pathlib import Path

import pytest

from cycleplotter.main import plot


@pytest.mark.parametrize(
    argnames=["fixture_path"],
    argvalues=[
        ("includes_other_data.xml",),
        ("beginning.xml",),
        ("end.xml",),
        ("pregnancy.xml",),
    ],
)
def test_plot(
    tmp_path,
    fixture_path,
):
    image_output_path: Path = tmp_path / "test_output.png"
    assert not image_output_path.exists()
    plot(
        input_data_path=f"tests/fixtures/{fixture_path}", output_path=image_output_path
    )
    assert image_output_path.exists()
