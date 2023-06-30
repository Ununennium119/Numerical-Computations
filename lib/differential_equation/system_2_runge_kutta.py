import math
from typing import Callable


class System2RungeKutta:
    """A class used to solve system of two differential equations with Runge Kutta's method"""

    def __init__(self,
                 f_1: Callable[[float, float, float], float],
                 f_2: Callable[[float, float, float], float],
                 start: float,
                 end: float,
                 step: float,
                 y_0: float,
                 p_0: float):
        self._f_1: Callable[[float, float, float], float] = f_1
        self._f_2: Callable[[float, float, float], float] = f_2
        self._start: float = start
        self._end: float = end
        self._step: float = step
        self._y_0: float = y_0
        self._p_0: float = p_0
        self._y: list[float] = []
        self._p: list[float] = []

    @property
    def y(self):
        return self._y.copy()

    @property
    def p(self):
        return self._p.copy()

    def calc(self, order: int) -> tuple[list[float], list[float]]:
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

        self._y.clear()
        self._y.append(self._y_0)
        self._p.append(self._p_0)
        for i in range(math.floor((self._end - self._start) / self._step + 0.5)):
            x = self._start + self._step * i
            y = self._y[-1]
            p = self._p[-1]
            y, p = func(x, y, p)
            self._y.append(y)
            self._p.append(p)

        return self.y, self.p

    def _calc_1st_order(self, x, y, p) -> tuple[float, float]:
        k_1 = self._step * self._f_1(x, y, p)
        l_1 = self._step * self._f_2(x, y, p)
        next_y = y + k_1
        next_p = p + l_1
        return next_y, next_p

    def _calc_2nd_order(self, x, y, p) -> tuple[float, float]:
        k_1 = self._step * self._f_1(x, y, p)
        l_1 = self._step * self._f_2(x, y, p)
        k_2 = self._step * self._f_1(x + self._step, y + k_1, p + l_1)
        l_2 = self._step * self._f_2(x + self._step, y + k_1, p + l_1)
        next_y = y + (k_1 + k_2) / 2
        next_p = p + (l_1 + l_2) / 2
        return next_y, next_p

    def _calc_3rd_order(self, x, y, p) -> tuple[float, float]:
        k_1 = self._step * self._f_1(x, y, p)
        l_1 = self._step * self._f_2(x, y, p)
        k_2 = self._step * self._f_1(x + self._step / 2, y + k_1 / 2, p + l_1 / 2)
        l_2 = self._step * self._f_2(x + self._step / 2, y + k_1 / 2, p + l_1 / 2)
        k_3 = self._step * self._f_1(x + self._step, y - k_1 + 2 * k_2, p - l_1 + 2 * l_2)
        l_3 = self._step * self._f_2(x + self._step, y - k_1 + 2 * k_2, p - l_1 + 2 * l_2)
        next_y = y + k_1 / 6 + 2 * k_2 / 3 + k_3 / 6
        next_p = p + l_1 / 6 + 2 * l_2 / 3 + l_3 / 6
        return next_y, next_p

    def _calc_4th_order(self, x, y, p) -> tuple[float, float]:
        k_1 = self._step * self._f_1(x, y, p)
        l_1 = self._step * self._f_2(x, y, p)
        k_2 = self._step * self._f_1(x + self._step / 2, y + k_1 / 2, p + l_1 / 2)
        l_2 = self._step * self._f_2(x + self._step / 2, y + k_1 / 2, p + l_1 / 2)
        k_3 = self._step * self._f_1(x + self._step / 2, y + k_2 / 2, p + l_2 / 2)
        l_3 = self._step * self._f_2(x + self._step / 2, y + k_2 / 2, p + l_2 / 2)
        k_4 = self._step * self._f_1(x + self._step, y + k_3, p + l_3)
        l_4 = self._step * self._f_2(x + self._step, y + k_3, p + l_3)
        next_y = y + k_1 / 6 + k_2 / 3 + k_3 / 3 + k_4 / 6
        next_p = p + l_1 / 6 + l_2 / 3 + l_3 / 3 + l_4 / 6
        return next_y, next_p
