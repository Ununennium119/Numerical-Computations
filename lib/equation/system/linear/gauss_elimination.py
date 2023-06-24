from typing import Optional


class GaussElimination:
    """A class used for solving system of linear equations using Gauss Elimination"""

    def __init__(self,
                 coefficient: list[list[float]],
                 constant: list[float]):
        if len(coefficient) != len(coefficient[0]) or len(coefficient) != len(constant):
            raise ValueError('coefficient matrix and constant vector should have the same size.')
        self._coefficient: list[list[float]] = coefficient
        self._constant: list[float] = constant
        self._eliminated_matrix: Optional[list[list[float]]] = None
        self._eliminated_constant: Optional[list[float]] = None

    def _eliminate(self):
        self._eliminated_matrix = [row.copy() for row in self._coefficient]
        self._eliminated_constant = self._constant.copy()
        size = len(self._constant)
        for i in range(size - 1):
            for j in range(i + 1, size):
                ratio = -self._eliminated_matrix[j][i] / self._eliminated_matrix[i][i]
                for k in range(i, size):
                    self._eliminated_matrix[j][k] += self._eliminated_matrix[i][k] * ratio
                self._eliminated_constant[j] += self._eliminated_constant[i] * ratio
        for i in range(size - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                ratio = -self._eliminated_matrix[j][i] / self._eliminated_matrix[i][i]
                for k in range(i, j, -1):
                    self._eliminated_matrix[j][k] += self._eliminated_matrix[i][k] * ratio
                self._eliminated_constant[j] += self._eliminated_constant[i] * ratio

    def calc_determinant(self) -> float:
        self._eliminate()

        determinant = 1
        for i in range(len(self._eliminated_matrix)):
            determinant *= self._eliminated_matrix[i][i]

        return determinant

    def calc_inverse(self) -> list[list[float]]:
        self._eliminated_matrix = [row.copy() for row in self._coefficient]
        size = len(self._constant)

        inverse = []
        for i in range(size):
            row = []
            for j in range(size):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            inverse.append(row)

        for i in range(size - 1):
            for j in range(i + 1, size):
                ratio = -self._eliminated_matrix[j][i] / self._eliminated_matrix[i][i]
                for k in range(0, size):
                    self._eliminated_matrix[j][k] += self._eliminated_matrix[i][k] * ratio
                    inverse[j][k] += inverse[i][k] * ratio
        for i in range(size - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                ratio = -self._eliminated_matrix[j][i] / self._eliminated_matrix[i][i]
                for k in range(size - 1, -1, -1):
                    self._eliminated_matrix[j][k] += self._eliminated_matrix[i][k] * ratio
                    inverse[j][k] += inverse[i][k] * ratio
        for i in range(size):
            for j in range(size):
                inverse[i][j] /= self._eliminated_matrix[i][i]

        return inverse

    def solve(self) -> list[float]:
        self._eliminate()

        x = []
        for i in range(len(self._constant)):
            x.append(self._eliminated_constant[i] / self._eliminated_matrix[i][i])
        return x
