from lib import GaussSeidel, Jacobi


def main():
    gauss_seidel = GaussSeidel(
        [[5, 3, 4],
         [3, 6, 4],
         [4, 4, 5]],
        [12, 13, 13],
        [0, 0, 0],
        100,
        3,
        0.001
    )
    gauss_seidel.solve()
    gauss_seidel.print_result()

    print("----------------------------------------")

    jacobi = Jacobi(
        [[5, 3, 4],
         [3, 6, 4],
         [4, 4, 5]],
        [12, 13, 13],
        [0, 0, 0],
        100,
        5,
        0.001
    )
    jacobi.solve()
    jacobi.print_result()


if __name__ == '__main__':
    main()
