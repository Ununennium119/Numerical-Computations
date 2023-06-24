from lib.integral.integral import Integral


class TrapezoidalIntegral(Integral):
    """A class used to calculate integral using Trapezoidal rule"""

    def __init__(self, y: list[float], h: float):
        super(TrapezoidalIntegral, self).__init__(y, h)

    def calc_integral(self) -> float:
        self._result = (self._y[0] + self._y[-1]) / 2
        for i in range(1, len(self._y) - 1):
            self._result += self._y[i]
        self._result *= self._h

        return self._result
