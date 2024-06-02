import pytest

from cycleplotter.interfaceadapters.cli.argparser import SizeParseError, parse_size
from cycleplotter.usecases.plotter import SIZE_A4, SIZE_LETTER, Size


@pytest.mark.parametrize(
    argnames=["input_size_str", "expected_size_object"],
    argvalues=[
        ("a4", SIZE_A4),
        ("letter", SIZE_LETTER),
        ("600x400px", Size(width_inches=6, height_inches=4)),
        ("6x4in", Size(width_inches=6, height_inches=4)),
        ("15.24x10.16cm", Size(width_inches=6, height_inches=4)),
    ],
)
def test_parse_size(
    input_size_str: str,
    expected_size_object: Size,
):
    actual_size_object = parse_size(input_size_str)
    assert (
        pytest.approx(actual_size_object.width_inches)
        == expected_size_object.width_inches
    )
    assert (
        pytest.approx(actual_size_object.height_inches)
        == expected_size_object.height_inches
    )


@pytest.mark.parametrize(
    argnames=["input_size_str"],
    argvalues=[
        ("5cmx5cm",),
        ("12x12dp",),
        ("hello",),
        ("",),
    ],
)
def test_parse_size_error(input_size_str: str):
    with pytest.raises(SizeParseError):
        parse_size(input_size_str)
