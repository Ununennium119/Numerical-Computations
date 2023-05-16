import math
from typing import Callable, Optional


class Newton:
    """A class used for solving 2-var nonlinear equations using newton method"""

    def __init__(self,
                 funcs: list[Callable[[list[float]], float]],
                 jacob: list[list[Callable[[list[float]], float]]],
                 x_0: list[float],
                 steps: int,
                 round_digits: int = 3,
                 error: float = 10e-10):
        size = len(funcs)
        if len(jacob) != size or len(jacob[0]) != size or len(x_0) != size:
            raise ValueError("size of funcs, jacobian and x_0 should be equal!")
        if steps <= 0:
            raise ValueError("steps should be positive!")
        if round_digits < 0:
            raise ValueError("round_digits cannot be negative!")

        self._funcs: list[Callable[[list[float]], float]] = funcs
        self._jacob: list[list[Callable[[list[float]], float]]] = jacob
        self._x: list[float] = x_0
        self._steps: int = steps
        self._round_digits: int = round_digits
        self._error: float = error
        self.x_steps: list[list[float]] = []

    @property
    def error(self) -> Optional[float]:
        if len(self.x_steps) < 2:
            return None
        else:
            return math.sqrt(sum(((a_i - b_i) ** 2 for a_i, b_i in zip(self.x_steps[-1], self.x_steps[-2]))))

    def solve(self) -> list[float]:
        """Return solution of the equation."""
        for i in range(self._steps):
            x = self._x
            delta_x = self._funcs[0](x) * self._jacob[1][1](x) - self._jacob[0][1](x) * self._funcs[1](x)
            delta_y = self._jacob[0][0](x) * self._funcs[1](x) - self._funcs[0](x) * self._jacob[1][0](x)
            det_jacob = self._jacob[0][0](x) * self._jacob[1][1](x) - self._jacob[0][1](x) * self._jacob[1][0](x)
            x[0] -= round(delta_x / det_jacob, self._round_digits)
            x[1] -= round(delta_y / det_jacob, self._round_digits)
            self.x_steps.append(self._x.copy())
        return self._x

    def print_result(self):
        print(f"answer = {self.x_steps[-1]}")
        print("steps:")
        for index, step in enumerate(self.x_steps):
            print(f"\tx({index + 1}) = {step}")
        print(f"error = {self.error}")
