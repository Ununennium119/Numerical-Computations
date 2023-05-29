from lib import Newton


def main():
    newton = Newton(
        [f, g],
        [[f_x1, f_x2],
         [g_x1, g_x2]],
        [1, 1],
        6,
        3
    )
    newton.solve()
    newton.print_result()


def f(x: list[float]) -> float:
    return x[0] ** 2 + x[1] ** 2 - 25


def g(x: list[float]) -> float:
    return x[0] ** 2 - x[1] ** 2 - 5


def f_x1(x: list[float]) -> float:
    return 2 * x[0]


def f_x2(x: list[float]) -> float:
    return 2 * x[1]


def g_x1(x: list[float]) -> float:
    return 2 * x[0]


def g_x2(x: list[float]) -> float:
    return -2 * x[1]


if __name__ == '__main__':
    main()
