from typing import Callable

from lib.root.bracketing.bracketing import BracketingRoot


class FalsePositionRoot(BracketingRoot):
    """A class used for calculating roots of functions with Bisection method."""

    def __init__(self,
                 start: float,
                 end: float,
                 func: Callable[[float], float],
                 error: float = 10e-7,
                 max_iterations: int = 100):
        super(FalsePositionRoot, self).__init__(start, end, func, error, max_iterations)

    def _get_next_point(self) -> float:
        start_value = self._func(self._start)
        end_value = self._func(self._end)
        return (self._start * end_value - self._end * start_value) / (end_value - start_value)

    def _calc_error(self) -> float:
        return abs(self._func(self._root))
