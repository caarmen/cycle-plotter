import argparse

from cycleplotter.interfaceadapters.factory import Source, create_parser
from cycleplotter.usecases import extract_cycle_durations, plotter


def main():
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
    args = arg_parser.parse_args()
    parser = create_parser(args.source)
    cycle_durations = extract_cycle_durations(parser, args.input_file)
    plotter.plot_cycle_durations(
        cycle_durations=cycle_durations,
        output_path=args.output_file,
        config=plotter.PlotConfig(
            duration_axis=args.axis,
        ),
    )


if __name__ == "__main__":
    main()
