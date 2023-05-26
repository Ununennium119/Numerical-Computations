from typing import Callable


class SecantRoot:
    """A class used for calculating roots of functions with Secant method."""

    def __init__(self,
                 x_0: float,
                 x_1: float,
                 func: Callable[[float], float],
                 error: float = 10e-7,
                 max_iterations: int = 100):
        self._points: list[float] = [x_0, x_1]
        self._func: Callable[[float], float] = func
        self._error: float = error
        self._max_iterations: int = max_iterations

    @property
    def points(self) -> list[float]:
        """Get the points calculated to find root."""
        return self._points.copy()

    @property
    def root(self):
        """Get the calculated root."""
        return self._points[-1]

    @property
    def initial_guess(self) -> float:
        """Get or set the initial guess."""
        return self._points[0]

    @initial_guess.setter
    def initial_guess(self, value: float):
        self._points = [value]

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

    def find_root(self) -> float:
        """Return root of the given function."""
        for i in range(self._max_iterations):
            x_n1 = self._points[-1]
            x_n2 = self._points[-2]
            f = self._func
            next_point = (x_n2 * f(x_n1) - x_n1 * f(x_n2)) / (f(x_n1) - f(x_n2))
            self._points.append(next_point)
            if abs(self._points[-1] - self._points[-2]) < self._error:
                break

        return self._points[-1]
