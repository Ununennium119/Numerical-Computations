from lib.equation.linear.gauss_seidel import GaussSeidel
from lib.equation.linear.jacobi import Jacobi


def main():
    jacobi = Jacobi(
        [[4, 1, -2],
         [-1, 4, -1],
         [1, -1, 4]],
        [4, 0, 4],
        [0, 0, 0],
        3,
        3
    )
    jacobi.solve()
    jacobi.print_result()

    print("----------------------------------------")

    gauss_seidel = GaussSeidel(
        [[4, 1, -2],
         [-1, 4, -1],
         [1, -1, 4]],
        [4, 0, 4],
        [0, 0, 0],
        3,
        3
    )
    gauss_seidel.solve()
    gauss_seidel.print_result()


if __name__ == '__main__':
    main()
