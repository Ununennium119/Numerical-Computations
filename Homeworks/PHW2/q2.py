import math

from lib import BisectionRoot, FalsePositionRoot, FixedPointRoot, NewtonRoot, SecantRoot


def main():
    bisection = BisectionRoot(start=-1, end=0, func=f, error=1e-3, max_iterations=100)
    print(f"Bisection: x = {bisection.find_root()}, steps = {bisection.iterations_count}")

    false_position = FalsePositionRoot(start=-1, end=0, func=f, error=1e-3, max_iterations=100)
    print(f"False Position: x = {false_position.find_root()}, steps = {false_position.iterations_count}")

    newton = NewtonRoot(initial_guess=-0.5, func=f, diff=diff_f, error=1e-3, max_iterations=100)
    print(f"Newton: x = {newton.find_root()}, steps = {newton.iterations_count}")

    secant = SecantRoot(x_0=-1, x_1=0, func=f, error=1e-3, max_iterations=100)
    print(f"Secant: x = {secant.find_root()}, steps = {secant.iterations_count}")

    fixed_point = FixedPointRoot(initial_guess=-0.5, func=f_fixed, error=1e-3, max_iterations=100)
    print(f"Fixed-Point: x = {fixed_point.find_root()}, steps = {fixed_point.iterations_count}")

    print("------------------------------------------------------------------")

    bisection = BisectionRoot(start=math.pi / 2, end=math.pi, func=g, error=1e-3, max_iterations=100)
    print(f"Bisection: x = {bisection.find_root()}, steps = {bisection.iterations_count}")

    false_position = FalsePositionRoot(start=math.pi / 2, end=math.pi, func=g, error=1e-3, max_iterations=100)
    print(f"False Position: x = {false_position.find_root()}, steps = {false_position.iterations_count}")

    newton = NewtonRoot(initial_guess=3 / 4 * math.pi, func=g, diff=diff_g, error=1e-3, max_iterations=100)
    print(f"Newton: x = {newton.find_root()}, steps = {newton.iterations_count}")

    secant = SecantRoot(x_0=math.pi / 2, x_1=math.pi, func=g, error=1e-3, max_iterations=100)
    print(f"Secant: x = {secant.find_root()}, steps = {secant.iterations_count}")

    fixed_point = FixedPointRoot(initial_guess=3 / 4 * math.pi, func=g_fixed, error=1e-3, max_iterations=100)
    print(f"Fixed-Point: x = {fixed_point.find_root()}, steps = {fixed_point.iterations_count}")


def f(x: float) -> float:
    return -2.75 * x ** 3 + 18 * x ** 2 - 21 * x - 12


def diff_f(x: float) -> float:
    return -8.25 * x ** 2 + 36 * x - 21


def f_fixed(x: float) -> float:
    return 12 / (-2.75 * x ** 2 + 18 * x - 21)


def g(x: float) -> float:
    return math.sin(x) - 0.1 * x


def diff_g(x: float) -> float:
    return math.cos(x) - 0.1


def g_fixed(x: float) -> float:
    return math.pi - math.asin(0.1 * x)


if __name__ == '__main__':
    main()
