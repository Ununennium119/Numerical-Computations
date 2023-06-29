from lib import LagrangeInterpolation, NewtonInterpolation


def main():
    print('-------------------------A-------------------------')
    print('Newton:')
    newton_interpolation = NewtonInterpolation(
        x=[1, 2, 2.5, 3, 4, 5],
        y=[0, 5, 7, 6.5, 2, 0]
    )
    newton_interpolation.calc_interpolation()
    print(f'f(3.4) ≈ {newton_interpolation.approx_point(3.4)}')
    newton_interpolation.print_interpolation()

    print()

    print('Lagrange:')
    lagrange_interpolation = LagrangeInterpolation(
        x=[1, 2, 2.5, 3, 4, 5],
        y=[0, 5, 7, 6.5, 2, 0]
    )
    lagrange_interpolation.calc_interpolation()
    print(f'f(3.4) ≈ {newton_interpolation.approx_point(3.4)}')
    lagrange_interpolation.print_interpolation()


if __name__ == '__main__':
    main()
