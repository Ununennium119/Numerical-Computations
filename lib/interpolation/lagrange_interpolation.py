from lib.interpolation.poly_interpolation import PolyInterpolation


class LagrangeInterpolation(PolyInterpolation):
    """A class used to calculate polynomial interpolation using lagrange's method"""

    def __init__(self, x: list[float], y: list[float]):
        super(LagrangeInterpolation, self).__init__(x, y)

    def print_interpolation(self):
        for i, coefficient in enumerate(self._interpolation):
            print(f'{coefficient}', end='')
            for j, x_j in enumerate(self._x):
                if i == j:
                    continue
                print(f'(x - {x_j})', end='')
            if i != len(self._interpolation) - 1:
                print(f' + ', end='')
        print()

    def calc_interpolation(self):
        for i in range(len(self._x)):
            divisor = 1
            for j in range(len(self._x)):
                if i == j:
                    continue
                divisor *= self._x[i] - self._x[j]
            self._interpolation.append(self._y[i] / divisor)
