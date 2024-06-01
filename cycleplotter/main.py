import argparse

from cycleplotter import plotter
from cycleplotter.parser import factory


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "input_file",
        help="path to export.xml file exported from Apple Health",
    )
    arg_parser.add_argument(
        "output_file",
        help="path to image file to export",
    )
    args = arg_parser.parse_args()
    parser = factory("apple")
    cycle_durations = parser.parse(args.input_file)
    plotter.plot_cycle_durations(
        cycle_durations=cycle_durations, output_path=args.output_file
    )


if __name__ == "__main__":
    main()
