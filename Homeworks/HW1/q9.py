import math

from lib import NewtonRoot


def main():
    newton_root: NewtonRoot = NewtonRoot(2, func_1, diff_func_1, 10e-4, 3)
    print(newton_root.find_root())
    print(newton_root.points)
    print(newton_root.iterations_count)


def func_1(x: float) -> float:
    return math.cos(x) + math.exp(x) - 3


def diff_func_1(x: float) -> float:
    return -math.sin(x) + math.exp(x)


if __name__ == '__main__':
    main()
