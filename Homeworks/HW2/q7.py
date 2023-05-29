import math

from lib import Newton


def main():
    newton = Newton(
        [f, g],
        [[f_x1, f_x2],
         [g_x1, g_x2]],
        [0, 0],
        5,
        3
    )
    newton.solve()
    newton.print_result()


def f(x: list[float]) -> float:
    return x[0] - math.cos(x[1]) / 2


def g(x: list[float]) -> float:
    return x[1] - math.sin(x[0]) / 2


def f_x1(x: list[float]) -> float:
    return 1


def f_x2(x: list[float]) -> float:
    return math.sin(x[1]) / 2


def g_x1(x: list[float]) -> float:
    return -math.cos(x[0]) / 2


def g_x2(x: list[float]) -> float:
    return 1


if __name__ == '__main__':
    main()
