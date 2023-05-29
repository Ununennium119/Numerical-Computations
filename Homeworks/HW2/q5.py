from lib import GaussSeidel


def main():
    gauss_seidel = GaussSeidel(
        [[1, -2],
         [2, 1]],
        [4, 3],
        [0, 0],
        100,
        3
    )
    gauss_seidel.solve()
    gauss_seidel.print_result()

    print("----------------------------------------")

    gauss_seidel = GaussSeidel(
        [[2, 1],
         [1, -2]],
        [3, 4],
        [0, 0],
        100,
        3
    )
    gauss_seidel.solve()
    gauss_seidel.print_result()


if __name__ == '__main__':
    main()
