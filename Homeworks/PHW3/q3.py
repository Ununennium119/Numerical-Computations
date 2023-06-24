import math
from lib import RungeKutta


def main():
    runge_kutta = RungeKutta(
        f=f,
        start=0,
        end=1,
        step=0.25,
        y_0=1
    )

    for i in range(1, 5):
        runge_kutta.calc(i)
        print(runge_kutta.result)


def f(x: float, y: float) -> float:
    return (1 + 2 * x) * math.sqrt(y)


if __name__ == '__main__':
    main()
