import math

from lib import Newton


def main():
    print("---------- A ----------")
    newton = Newton(
        [f_a, g_a],
        [[f_a_x1, f_a_x2],
         [g_a_x1, g_a_x2]],
        [1, 1],
        100,
        3,
        1e-3
    )
    print(f"x = {newton.solve()}")

    print()

    print("---------- B ----------")
    newton = Newton(
        [f_b, g_b],
        [[f_b_x1, f_b_x2],
         [g_b_x1, g_b_x2]],
        [2, 0.5],
        100,
        3,
        1e-3
    )
    print(f"x = {newton.solve()}")


def f_a(x: list[float]) -> float:
    return math.sin(x[0]) + 3 * math.cos(x[1]) - 2


def f_a_x1(x: list[float]) -> float:
    return math.cos(x[0])


def f_a_x2(x: list[float]) -> float:
    return -3 * math.sin(x[1])


def g_a(x: list[float]) -> float:
    return math.cos(x[0]) - math.sin(x[1]) + 0.2


def g_a_x1(x: list[float]) -> float:
    return -math.sin(x[0])


def g_a_x2(x: list[float]) -> float:
    return -math.cos(x[1])


def f_b(x: list[float]) -> float:
    return x[0] + 2 * x[1] - 3


def f_b_x1(x: list[float]) -> float:
    return 1


def f_b_x2(x: list[float]) -> float:
    return 2


def g_b(x: list[float]) -> float:
    return 2 * x[0] ** 2 + x[1] ** 2 - 5


def g_b_x1(x: list[float]) -> float:
    return 4 * x[0]


def g_b_x2(x: list[float]) -> float:
    return 2 * x[1]


if __name__ == '__main__':
    main()
