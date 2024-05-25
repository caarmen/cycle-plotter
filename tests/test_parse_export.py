import pytest

from cycleplotter.main import parse_export


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

    with open(f"tests/fixtures/{fixture_path}") as xml_file:
        xml_content = xml_file.read()
    cycle_durations = parse_export(xml_content)
    assert len(cycle_durations) == expected_cycle_count
