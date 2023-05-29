from lib import GaussSeidel


def main():
    gauss_seidel = GaussSeidel(
        [[1, 0, -1],
         [-0.5, 1, 0.25],
         [1, -0.5, 1]],
        [0.2, -1.425, 2],
        [0, 0, 0],
        300,
        3,
        0.01
    )
    gauss_seidel.solve()
    gauss_seidel.print_result()

    print("----------------------------------------")

    gauss_seidel = GaussSeidel(
        [[1, 0, -2],
         [-0.5, 1, -0.25],
         [1, -0.5, 1]],
        [0.2, -1.425, 2],
        [0, 0, 0],
        300,
        2,
        0.01
    )
    gauss_seidel.solve()
    gauss_seidel.print_result()


if __name__ == '__main__':
    main()
