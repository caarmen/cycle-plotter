from cycleplotter.interfaceadapters.cli.argparser import CliArgs, parse_args
from cycleplotter.interfaceadapters.cycledataparser import create_cycle_data_parser
from cycleplotter.usecases import CycleDataParser, extract_cycle_durations, plotter


def main():
    args: CliArgs = parse_args()
    cycle_data_parser: CycleDataParser = create_cycle_data_parser(args.source)
    cycle_durations = extract_cycle_durations(cycle_data_parser, args.input_file)
    plotter.plot_cycle_durations(
        cycle_durations=cycle_durations,
        output_path=args.output_file,
        config=plotter.PlotConfig(
            duration_axis=args.axis,
        ),
    )


if __name__ == "__main__":
    main()
