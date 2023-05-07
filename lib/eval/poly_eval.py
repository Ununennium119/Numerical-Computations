class PolyEval:
    """A class used for evaluating value of polynomials"""

    NO_ROUND = 0
    FLOOR = 1
    ROUND = 2

    def __init__(self, coefficients: list[float], round_mode: int = NO_ROUND, round_digits: int = 3):
        self._coefficients: list[float] = coefficients
        self._round_mode: int = round_mode
        self._round_digits: int = round_digits

    @staticmethod
    def _floor(x: float, digits: int) -> float:
        s = repr(x).split('.')
        if len(s) == 1:
            return float(s[0])
        return float(s[0] + '.' + s[1][:digits])

    def evaluate(self, x: float) -> float:
        """Return value of polynomial in x."""
        value: float = self._coefficients[0]
        def round_func(y: float, _) -> float: return y
        if self._round_mode == self.FLOOR:
            round_func = self._floor
        elif self._round_mode == self.ROUND:
            round_func = round
        for i in range(1, len(self._coefficients)):
            value = round_func(value * x + self._coefficients[i], self._round_digits)
        return value
