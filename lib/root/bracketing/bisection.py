from typing import Callable

from lib.root.bracketing.bracketing import BracketingRoot


class BisectionRoot(BracketingRoot):
    """A class used for calculating roots of functions with Bisection method."""

    def __init__(self,
                 start: float,
                 end: float,
                 func: Callable[[float], float],
                 error: float = 10e-7,
                 max_iterations: int = 100):
        super(BisectionRoot, self).__init__(start, end, func, error, max_iterations)

    def _get_next_point(self) -> float:
        return (self._start + self._end) / 2

    def _calc_error(self) -> float:
        return abs(self._start - self._end) / 2
