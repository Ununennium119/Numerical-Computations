import math
from typing import Callable


class GradientDescent:
    """A class used for calculating roots of functions with Gradient Descent method."""

    def __init__(self,
                 initial_guess: list[float],
                 alpha: float,
                 gradient: list[Callable[[list[float]], float]],
                 error: float = None,
                 max_iterations: int = 100):
        self._points: list[list[float]] = [initial_guess]
        self._alpha: float = alpha
        self._gradient: list[Callable[[list[float]], float]] = gradient
        self._error: float = error
        self._max_iterations: int = max_iterations

    @property
    def points(self) -> list[list[float]]:
        """Get the points calculated to find root."""
        return self._points.copy()

    @property
    def root(self):
        """Get the calculated root."""
        return self._points[-1]

    @property
    def initial_guess(self) -> list[float]:
        """Get or set the initial guess."""
        return self._points[0]

    @initial_guess.setter
    def initial_guess(self, value: list[float]):
        self._points = [value]

    @property
    def alpha(self) -> float:
        """Get or set the alpha."""
        return self._alpha

    @alpha.setter
    def alpha(self, value: float):
        self._alpha = value

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
        return len(self._points) - 1

    def find_root(self) -> list[float]:
        """Return root of the given function."""
        for i in range(self._max_iterations):
            current_point = self._points[-1]
            next_point = []
            for j in range(len(current_point)):
                next_point.append(current_point[j] - self.alpha * self._gradient[j](current_point))
            self._points.append(next_point)
            if self._error:
                is_precise = True
                for j in range(len(current_point)):
                    if abs(next_point[j] - current_point[j]) > self._error:
                        is_precise = False
                        break
                if is_precise:
                    break

        return self._points[-1]
