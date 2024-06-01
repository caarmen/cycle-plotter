import enum

from cycleplotter.usecases.parser.applehealth import AppleHealthParser


class Parser(enum.Enum):
    APPLE = "apple"


def create_parser(parser: Parser):
    if parser == Parser.APPLE:
        return AppleHealthParser()
