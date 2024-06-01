from abc import ABC, abstractmethod

from cycleplotter.model import CycleDuration


class Parser(ABC):
    @abstractmethod
    def parse(input_data_path: str) -> list[CycleDuration]:
        raise NotImplementedError
