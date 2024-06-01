from abc import ABC, abstractmethod

from cycleplotter.entities.cycle_duration import CycleDuration


class Parser(ABC):
    @abstractmethod
    def parse(input_data_path: str) -> list[CycleDuration]:
        raise NotImplementedError
