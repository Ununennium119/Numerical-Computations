from lib.equation.linear.gauss_seidel import GaussSeidel


def main():
    gauss_seidel = GaussSeidel(
        [[1, 0, -1],
         [-0.5, 1, 0.25],
         [1, -0.5, 1]],
        [0.2, -1.425, 2],
        [0.9, 0.8, 0.7],
        300,
        3
    )

    print(gauss_seidel.solve())
    print(gauss_seidel.x_steps)
    gauss_seidel = GaussSeidel(
        [[1, 0, -2],
         [-0.5, 1, -0.25],
         [1, -0.5, 1]],
        [0.2, -1.425, 2],
        [0.9, 0.8, 0.7],
        300,
        2
    )
    print(gauss_seidel.solve())
    print(gauss_seidel.x_steps)


if __name__ == '__main__':
    main()
