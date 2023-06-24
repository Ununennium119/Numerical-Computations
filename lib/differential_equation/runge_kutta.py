import math
from typing import Callable


class RungeKutta:
    """A class used to solve differential equations with Runge Kutta's method"""

    def __init__(self, f: Callable[[float, float], float], start: float, end: float, step: float, y_0: float):
        self._f: Callable[[float, float], float] = f
        self._start: float = start
        self._end: float = end
        self._step: float = step
        self._y_0: float = y_0
        self._result: list[float] = []

    @property
    def result(self):
        return self._result.copy()

    def calc(self, order: int) -> list[float]:
        if order < 1:
            order = 1
        elif order > 4:
            order = 4

        match order:
            case 1:
                func = self._calc_1st_order
            case 2:
                func = self._calc_2nd_order
            case 3:
                func = self._calc_3rd_order
            case _:
                func = self._calc_4th_order

        self._result.clear()
        self._result.append(self._y_0)
        for i in range(math.floor((self._end - self._start) / self._step)):
            x = self._start + self._step * i
            y = self._result[-1]
            self._result.append(func(x, y))

        return self._result.copy()

    def _calc_1st_order(self, x, y) -> float:
        return y + self._step * self._f(x, y)

    def _calc_2nd_order(self, x, y) -> float:
        k_1 = self._step * self._f(x, y)
        k_2 = self._step * self._f(x + self._step, y + k_1)
        return y + (k_1 + k_2) / 2

    def _calc_3rd_order(self, x, y) -> float:
        k_1 = self._step * self._f(x, y)
        k_2 = self._step * self._f(x + self._step / 2, y + k_1 / 2)
        k_3 = self._step * self._f(x + self._step, y - k_1 + 2 * k_2)
        return y + k_1 / 6 + 2 * k_2 / 3 + k_3 / 6

    def _calc_4th_order(self, x, y) -> float:
        k_1 = self._step * self._f(x, y)
        k_2 = self._step * self._f(x + self._step / 2, y + k_1 / 2)
        k_3 = self._step * self._f(x + self._step / 2, y + k_2 / 2)
        k_4 = self._step * self._f(x + self._step, y + k_3)
        return y + k_1 / 6 + k_2 / 3 + k_3 / 3 + k_4 / 6
