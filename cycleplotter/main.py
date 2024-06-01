import argparse

from cycleplotter.usecases import Source, extract_cycle_durations, plotter


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "--input-file",
        help="path to export.xml file exported from Apple Health",
    )
    arg_parser.add_argument(
        "--output-file",
        help="path to image file to export",
    )
    arg_parser.add_argument(
        "--source",
        type=Source,
        choices=Source,
    )
    args = arg_parser.parse_args()
    cycle_durations = extract_cycle_durations(args.source, args.input_file)
    plotter.plot_cycle_durations(
        cycle_durations=cycle_durations, output_path=args.output_file
    )


if __name__ == "__main__":
    main()
