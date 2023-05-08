import math

from lib.equation.nonlinear.newton import Newton


def main():
    newton = Newton(
        [f, g],
        [[f_x1, f_x2],
         [g_x1, g_x2]],
        [0, 0],
        5,
        7
    )
    newton.solve()
    print(newton.x_steps)


def f(x: list[float]) -> float:
    return x[0] ** 2 - 10 * x[0] + x[1] ** 2 + 8


def g(x: list[float]) -> float:
    return x[0] * x[1] ** 2 + x[0] - 10 * x[1] + 8


def f_x1(x: list[float]) -> float:
    return 2 * x[0] - 10


def f_x2(x: list[float]) -> float:
    return 2 * x[1]


def g_x1(x: list[float]) -> float:
    return x[1] ** 2 + 1


def g_x2(x: list[float]) -> float:
    return 2 * x[0] * x[1] - 10


if __name__ == '__main__':
    main()
