from lib.equation.linear.gauss_seidel import GaussSeidel
from lib.equation.linear.jacobi import Jacobi


def main():
    gauss_seidel = GaussSeidel(
        [[5, 3, 4],
         [3, 6, 4],
         [4, 4, 5]],
        [12, 13, 13],
        [0, 0, 0],
        10,
        3
    )
    gauss_seidel.solve()
    print(gauss_seidel.x_steps)

    jacobi = Jacobi(
        [[5, 3, 4],
         [3, 6, 4],
         [4, 4, 5]],
        [12, 13, 13],
        [0, 0, 0],
        5,
        3
    )
    jacobi.solve()
    print(jacobi.x_steps)


if __name__ == '__main__':
    main()
