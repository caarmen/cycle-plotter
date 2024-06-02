import argparse
from typing import Protocol

from cycleplotter.interfaceadapters.config import Source
from cycleplotter.usecases import plotter


class CliArgs(Protocol):
    input_file: str
    output_file: str
    source: Source
    axis: plotter.DurationAxis


def parse_args() -> CliArgs:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-i",
        "--input-file",
        help="path to export.xml file exported from Apple Health",
        required=True,
    )
    arg_parser.add_argument(
        "-o",
        "--output-file",
        help="path to image file to export",
        required=True,
    )
    arg_parser.add_argument(
        "-s",
        "--source",
        type=Source,
        choices=Source,
        required=True,
    )
    arg_parser.add_argument(
        "-a",
        "--axis",
        type=plotter.DurationAxis,
        choices=plotter.DurationAxis,
        default=plotter.DurationAxis.BOTH,
        help="""Indicate the cycle durations on the x-axis 
(by horizontal spacing between points), y-axis (by their values), or both axes. 
Default %(default)s.
""",
    )
    return arg_parser.parse_args()
