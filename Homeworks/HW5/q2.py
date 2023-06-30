import math

from lib import System2RungeKutta


def main():
    runge_kutta = System2RungeKutta(
        f_1,
        f_2,
        0,
        0.3,
        0.1,
        -0.4,
        -0.6
    )
    runge_kutta.calc(4)
    print(runge_kutta.y)
    print(runge_kutta.p)


def f_1(x, y, p) -> float:
    return p


def f_2(x, y, p) -> float:
    return 2 * p - 2 * y + math.sinh(2 * x) * math.sin(x)


if __name__ == '__main__':
    main()
