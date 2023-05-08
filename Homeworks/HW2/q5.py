from lib.equation.linear.gauss_seidel import GaussSeidel
from lib.equation.linear.jacobi import Jacobi


def main():
    gauss_seidel = GaussSeidel(
        [[1, -2],
         [2, 1]],
        [4, 3],
        [0, 0],
        5,
        3
    )
    gauss_seidel.solve()
    print(gauss_seidel.x_steps)

    gauss_seidel = GaussSeidel(
        [[2, 1],
         [1, -2]],
        [3, 4],
        [0, 0],
        5,
        3
    )
    gauss_seidel.solve()
    print(gauss_seidel.x_steps)


if __name__ == '__main__':
    main()
