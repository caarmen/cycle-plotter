from cycleplotter.parser.applehealth import AppleHealthParser


def create_parser(name: str):
    if name == "applehealth":
        return AppleHealthParser()
    raise ValueError(f"{name} is not a known parser")
