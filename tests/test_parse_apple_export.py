import pytest

from cycleplotter.parser.factory import create_parser


@pytest.mark.parametrize(
    argnames=["fixture_path", "expected_cycle_count"],
    argvalues=[
        ("includes_other_data.xml", 6),
        ("beginning.xml", 18),
        ("end.xml", 15),
        ("pregnancy.xml", 6),
    ],
)
def test_parse_export(
    fixture_path: str,
    expected_cycle_count: int,
):

    parser = create_parser("applehealth")
    cycle_durations = parser.parse(f"tests/fixtures/{fixture_path}")
    assert len(cycle_durations) == expected_cycle_count
