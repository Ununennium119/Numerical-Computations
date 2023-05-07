class GaussSeidel:
    """A class used for solving linear equations"""

    def __init__(self, a: list[list[float]], b: list[float], x_0: list[float], steps: int, round_digits: int = 3):
        if len(a) == 0:
            raise ValueError("a is empty!")
        a_dim = len(a), len(a[0])
        if a_dim[0] != a_dim[1] or a_dim[0] != len(b) or a_dim[0] != len(x_0):
            raise ValueError("size of a, b and x_0 should be equal!")
        if steps <= 0:
            raise ValueError("steps should be positive!")
        if round_digits < 0:
            raise ValueError("round_digits cannot be negative!")

        self._A: list[list[float]] = a
        self._b: list[float] = b
        self._x: list[float] = x_0
        self._steps: int = steps
        self._round_digits: int = round_digits
        self.x_steps: list[list[float]] = []

    def solve(self):
        """Return solution of the equation."""
        self.x_steps = []
        for i in range(self._steps):
            for j in range(len(self._x)):
                self._x[j] = 0
                for k in range(len(self._x)):
                    if k == j:
                        continue
                    self._x[j] -= self._A[j][k] * self._x[k]
                self._x[j] += self._b[j]
                self._x[j] /= self._A[j][j]
                self._x[j] = round(self._x[j], self._round_digits)
            self.x_steps.append(self._x.copy())
        return self._x
