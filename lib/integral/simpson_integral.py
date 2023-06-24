from lib.integral.integral import Integral


class SimpsonIntegral(Integral):
    """A class used to calculate integral using Simpson's rule"""

    def __init__(self, y: list[float], h: float):
        super(SimpsonIntegral, self).__init__(y, h)

        if len(y) % 2 == 0:
            raise ValueError('y should have odd number of points.')

    def calc_integral(self) -> float:
        self._result = self._y[0] + self._y[-1]
        for i in range(1, len(self._y) - 1):
            if i % 2 == 0:
                self._result += 2 * self._y[i]
            else:
                self._result += 4 * self._y[i]
        self._result *= self._h / 3

        return self._result
