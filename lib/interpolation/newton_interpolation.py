from lib.interpolation.poly_interpolation import PolyInterpolation


class NewtonInterpolation(PolyInterpolation):
    """A class used to calculate polynomial interpolation using newton's method"""

    def __init__(self, x: list[float], y: list[float]):
        super(NewtonInterpolation, self).__init__(x, y)

    def print_interpolation(self):
        for i, coefficient in enumerate(self._interpolation):
            print(f'{coefficient}', end='')
            for j in range(i):
                print(f'(x - {self._x[j]})', end='')
            if i != len(self._interpolation) - 1:
                print(f' + ', end='')
        print()

    def calc_interpolation(self):
        self._interpolation.clear()

        delta_f: list[float] = self._y
        new_delta_f: list[float] = []
        self._interpolation.append(delta_f[0])
        for i in range(len(self._x) - 1):
            for j in range(len(delta_f) - 1):
                try:
                    diff = (delta_f[j + 1] - delta_f[j]) / (self._x[j + i + 1] - self._x[j])
                except IndexError as e:
                    print(i, j)
                    raise e
                new_delta_f.append(diff)
            delta_f = new_delta_f
            new_delta_f = []
            self._interpolation.append(delta_f[0])
