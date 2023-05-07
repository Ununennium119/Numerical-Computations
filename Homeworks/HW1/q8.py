from lib.root.bracketing.false_position import FalsePositionRoot


def main():
    false_position_root: FalsePositionRoot = FalsePositionRoot(-1, 0, func_1, 10e-4)
    print(false_position_root.find_root())
    print(false_position_root.iterations_count)
    for step in false_position_root.steps:
        print(step)


def func_1(x: float) -> float:
    return (((-11 / 4) * x + 18) * x - 21) * x - 12


if __name__ == '__main__':
    main()
