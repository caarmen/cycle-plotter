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
    args = arg_parser.parse_args()
    parser = create_parser(args.source)
    cycle_durations = extract_cycle_durations(parser, args.input_file)
    plotter.plot_cycle_durations(
        cycle_durations=cycle_durations, output_path=args.output_file
    )


if __name__ == "__main__":
    main()
