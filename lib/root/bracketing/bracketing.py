from abc import ABC, abstractmethod
from typing import Callable


class BracketingRoot(ABC):
    """A parent class used for calculating roots of functions with Bracketing methods."""

    def __init__(self,
                 start: float,
                 end: float,
                 func: Callable[[float], float],
                 error: float = 10e-7,
                 max_iterations: int = 100):
        self._start: float = start
        self._end: float = end
        self._steps: list[tuple[float, float]] = [(start, end)]
        self._func: Callable[[float], float] = func
        self._error: float = error
        self._max_iterations: int = max_iterations
        self._iteration_count: int = 0
        self._root: float = 0

    @property
    def root(self) -> float:
        """Get the calculated root."""
        return self._root

    @property
    def steps(self) -> list[tuple[float, float]]:
        return self._steps.copy()

    @property
    def error(self) -> float:
        """Get or set the desired error."""
        return self._error

    @error.setter
    def error(self, value: float):
        self._error = value

    @property
    def max_iterations(self) -> int:
        """Get or set max iterations used for finding root."""
        return self._max_iterations

    @max_iterations.setter
    def max_iterations(self, value: int):
        self._max_iterations = value

    @property
    def iterations_count(self) -> int:
        """Get iterations count used for finding root."""
        return self._iteration_count

    @abstractmethod
    def _get_next_point(self) -> float:
        pass

    @abstractmethod
    def _calc_error(self) -> float:
        pass

    def find_root(self) -> float:
        """Return root of the given function."""
        for self._iteration_count in range(self._max_iterations):
            self._root = self._get_next_point()
            if self._func(self._root) == 0 or self._calc_error() < self.error:
                break
            if self._func(self._start) * self._func(self._root) < 0:
                self._end = self._root
            else:
                self._start = self._root
            self._steps.append((self._start, self._end))
            if self._calc_error() < self._error:
                break
        self._iteration_count += 1

        return self._root
