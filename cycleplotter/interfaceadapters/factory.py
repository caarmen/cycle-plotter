import enum

from cycleplotter.interfaceadapters.parser.applehealth import AppleHealthParser
from cycleplotter.interfaceadapters.parser.withingshealthmate import (
    WithingsHealthmateParser,
)


class Source(enum.StrEnum):
    APPLE = "apple"
    WITHINGS = "withings"


def create_parser(parser: Source):
    if parser == Source.APPLE:
        return AppleHealthParser()
    if parser == Source.WITHINGS:
        return WithingsHealthmateParser()
