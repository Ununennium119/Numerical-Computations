from lib.root.bracketing.false_position import FalsePositionRoot


def main():
    false_position = FalsePositionRoot(0, 2, f, 0.01)
    print(false_position.find_root())
    print(false_position.steps)
    print([f(x) for x in false_position.steps])
    print(false_position.iterations_count)
    print(false_position.error)

    print('--------------------------------------------------')

    false_position = FalsePositionRoot(0, 1, f, 0.01)
    false_position.find_root()
    print(false_position.steps)
    print([f(x) for x in false_position.steps])
    print([x ** 2 for x in false_position.steps])
    print([x ** 3 for x in false_position.steps])
    print([x ** 4 for x in false_position.steps])

    print('--------------------------------------------------')

    false_position = FalsePositionRoot(-2, 0, f, 0.01)
    print(false_position.find_root())
    print(false_position.steps)
    print([f(x) for x in false_position.steps])
    print(false_position.iterations_count)
    print(false_position.error)

    print('--------------------------------------------------')

    false_position = FalsePositionRoot(-2.1, 0, f, 0.01)
    print(false_position.find_root())
    print(false_position.steps)
    print([f(x) for x in false_position.steps])
    print(false_position.iterations_count)
    print(false_position.error)


def f(x: float) -> float:
    return x ** 2 - 2


if __name__ == '__main__':
    main()
