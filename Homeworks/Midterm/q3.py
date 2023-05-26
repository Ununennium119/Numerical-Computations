from lib.root.iterative.newton import NewtonRoot


def main():
    newton_root: NewtonRoot = NewtonRoot(
        2,
        f,
        diff_f,
        0.001,
        100
    )
    newton_root.find_root()
    print(newton_root.points)


def f(x: float) -> float:
    return (x - 3) ** 2


def diff_f(x: float) -> float:
    return 2 * (x - 3)


if __name__ == '__main__':
    main()
