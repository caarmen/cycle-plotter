import enum

from cycleplotter.usecases.parser.applehealth import AppleHealthParser
from cycleplotter.usecases.parser.withingshealthmate import WithingsHealthmateParser


class Source(enum.StrEnum):
    APPLE = "apple"
    WITHINGS = "withings"


def create_parser(parser: Source):
    if parser == Source.APPLE:
        return AppleHealthParser()
    if parser == Source.WITHINGS:
        return WithingsHealthmateParser()
