from abc import ABC, abstractmethod


class PolyInterpolation(ABC):
    """An abstract class used to implementing polynomial interpolation methods"""

    def __init__(self, x: list[float], y: list[float]):
        if len(x) != len(y):
            raise ValueError('length of x and y should be equal.')
        if len(x) != len(set(x)):
            raise ValueError('values in x should be unique.')

        self._x: list[float] = x
        self._y: list[float] = y
        self._interpolation: list[float] = []

    @property
    def interpolation(self) -> list[float]:
        """Returns list of interpolation coefficients"""
        return self._interpolation.copy()

    @abstractmethod
    def print_interpolation(self) -> None:
        """Prints result of interpolation in human-readable form"""
        pass

    @abstractmethod
    def calc_interpolation(self) -> None:
        """Calculates interpolation"""
        pass

    @abstractmethod
    def approx_point(self, x: float) -> float:
        """Returns an Approximation of value of the function at the point x."""
        pass
