from lib import System2RungeKutta


def main():
    runge_kutta = System2RungeKutta(
        f_1,
        f_2,
        1,
        1.2,
        0.1,
        2,
        3
    )
    runge_kutta.calc(order=1)
    print(runge_kutta.y)
    print(runge_kutta.p)


def f_1(x, y, p) -> float:
    return p


def f_2(x, y, p) -> float:
    return - 3 * p / x - 2 * y / (x ** 2)


if __name__ == '__main__':
    main()
