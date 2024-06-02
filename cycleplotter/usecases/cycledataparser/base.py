import datetime as dt
from abc import ABC, abstractmethod


class CycleDataParser(ABC):
    @abstractmethod
    def parse(input_data_path: str) -> list[dt.datetime]:
        raise NotImplementedError
