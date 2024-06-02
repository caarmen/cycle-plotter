from cycleplotter.interfaceadapters.config import Source
from cycleplotter.interfaceadapters.cycledataparser.applehealth import AppleHealthParser
from cycleplotter.interfaceadapters.cycledataparser.withingshealthmate import (
    WithingsHealthmateParser,
)
from cycleplotter.usecases.cycledataparser.base import CycleDataParser


def create_cycle_data_parser(source: Source) -> CycleDataParser:
    if source == Source.APPLE:
        return AppleHealthParser()
    if source == Source.WITHINGS:
        return WithingsHealthmateParser()
