from lib import NewtonRoot
from lib.root.iterative.gradient_descent import GradientDescent


def main():
    newton_root: NewtonRoot = NewtonRoot(
        3.5,
        f,
        diff_f,
        0.1,
        100
    )
    newton_root.find_root()
    print(newton_root.points)

    gradient_descent = GradientDescent(
        [3.5],
        0.5,
        [grad_f],
        0.1,
        1000
    )
    gradient_descent.find_root()
    print(gradient_descent.points)


def f(x: float) -> float:
    return (x - 3) ** 2


def diff_f(x: float) -> float:
    return 2 * (x - 3)


def grad_f(x: list[float]) -> float:
    return 2 * (x[0] - 3)


if __name__ == '__main__':
    main()
