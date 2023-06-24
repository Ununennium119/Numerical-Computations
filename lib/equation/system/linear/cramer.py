class Cramer:
    """A class used for solving system of linear equations using Cramer's rule"""

    def __init__(self,
                 coefficient: list[list[float]],
                 constant: list[float]):
        if len(coefficient) != len(coefficient[0]) or len(coefficient) != len(constant):
            raise ValueError('coefficient matrix and constant vector should have the same size.')
        self._coefficient: list[list[float]] = coefficient
        self._constant: list[float] = constant

    @staticmethod
    def _calc_determinant(matrix: list[list[float]]) -> float:
        if len(matrix) != len(matrix[0]):
            raise ValueError('Matrix should be squared.')

        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        determinant: float = 0
        for i in range(len(matrix)):
            sub_matrix = []
            for j in range(1, len(matrix)):
                sub_matrix.append(matrix[j][0:i] + matrix[j][i + 1:])
            determinant += (-1) ** i * matrix[0][i] * Cramer._calc_determinant(sub_matrix)

        return determinant

    def solve(self) -> list[float]:
        x = []
        coefficient_determinant = Cramer._calc_determinant(self._coefficient)
        for i in range(len(self._coefficient)):
            replaces_matrix = []
            for j in range(0, len(self._coefficient)):
                replaces_matrix.append(self._coefficient[j][0:i] + [self._constant[j]] + self._coefficient[j][i + 1:])
            x.append(Cramer._calc_determinant(replaces_matrix) / coefficient_determinant)

        return x
