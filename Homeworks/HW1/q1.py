import math

from lib.root.iterative.newton import NewtonRoot


def main():
    newton_root: NewtonRoot = NewtonRoot(0.5, func_1, diff_func_1, 10e-4)
    print(newton_root.find_root())
    print(newton_root.points)
    print(newton_root.max_iterations)
    print(newton_root.iterations_count)


def func_1(x: float) -> float:
    return x - math.cos(x)


def diff_func_1(x: float) -> float:
    return 1 + math.sin(x)


if __name__ == '__main__':
    main()
