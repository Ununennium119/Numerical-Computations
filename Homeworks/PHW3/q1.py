from lib import LagrangeInterpolation, NewtonInterpolation


def main():
    newton_interpolation = NewtonInterpolation(
        x=[1, 2, 2.5, 3, 4, 5],
        y=[0, 5, 7, 6.5, 2, 0]
    )
    newton_interpolation.calc_interpolation()
    newton_interpolation.print_interpolation()

    lagrange_interpolation = LagrangeInterpolation(
        x=[1, 2, 2.5, 3, 4, 5],
        y=[0, 5, 7, 6.5, 2, 0]
    )
    lagrange_interpolation.calc_interpolation()
    lagrange_interpolation.print_interpolation()


if __name__ == '__main__':
    main()
