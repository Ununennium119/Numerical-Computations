from lib import Cramer, GaussElimination


def main():
    print('-------------------------A-------------------------')
    print('(7)')
    coefficient_7 = [[4, -8],
                     [1, 6]]
    constant_7 = [-24, 34]
    cramer = Cramer(
        coefficient_7,
        constant_7
    )
    print(f'x = {cramer.solve()} (cramer)')

    gauss_elimination = GaussElimination(
        [[4, -8],
         [1, 6]],
        [-24, 34]
    )
    print(f'x = {gauss_elimination.solve()} (gauss elimination)')

    print()

    print('(8)')
    coefficient_8 = [[10, 2, -1],
                     [-3, -5, 2],
                     [1, 1, 6]]
    constant_8 = [27, -61.5, -21.5]
    cramer = Cramer(
        coefficient_8,
        constant_8
    )
    print(f'x = {cramer.solve()} (cramer)')

    gauss_elimination = GaussElimination(
        [[10, 2, -1],
         [-3, -5, 2],
         [1, 1, 6]],
        [27, -61.5, -21.5]
    )
    print(f'x = {gauss_elimination.solve()} (gauss elimination)')

    print('\n-------------------------C-------------------------')
    print('(9)')
    matrix_9 = [[10, 2, -1],
                [-3, -6, 2],
                [1, 1, 5]]
    gauss_elimination = GaussElimination(
        matrix_9,
        [0, 0, 0]
    )
    print(f'determinant = {gauss_elimination.calc_determinant()}')

    print()

    print('(10)')
    matrix_10 = [[8, 2, -10],
                 [-9, 1, 3],
                 [15, -1, 6]]
    gauss_elimination = GaussElimination(
        matrix_10,
        [0, 0, 0]
    )
    print(f'determinant = {gauss_elimination.calc_determinant()}')

    print('\n-------------------------D-------------------------')
    print('(9)')
    matrix_9 = [[10, 2, -1],
                [-3, -6, 2],
                [1, 1, 5]]
    gauss_elimination = GaussElimination(
        matrix_9,
        [0, 0, 0]
    )
    print('inverse:')
    print_matrix(gauss_elimination.calc_inverse())

    print()

    print('(10)')
    matrix_10 = [[8, 2, -10],
                 [-9, 1, 3],
                 [15, -1, 6]]
    gauss_elimination = GaussElimination(
        matrix_10,
        [0, 0, 0]
    )
    print('inverse:')
    print_matrix(gauss_elimination.calc_inverse())


def print_matrix(matrix: list[list[float]]):
    for row in matrix:
        print(row)


if __name__ == '__main__':
    main()
