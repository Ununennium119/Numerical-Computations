from abc import ABC, abstractmethod


class Integral(ABC):
    """An abstract class used to implementing integral calculation methods"""

    def __init__(self, y: list[float], h: float):
        if len(y) < 2:
            raise ValueError('there should be at least 2 points to calculate integral.')

        self._y: list[float] = y
        self._h: float = h
        self._result: float = 0

    @property
    def result(self):
        return self._result

    @abstractmethod
    def calc_integral(self) -> float:
        pass
