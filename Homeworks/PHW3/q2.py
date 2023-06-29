from lib import TrapezoidalIntegral, SimpsonIntegral


def main():
    print('-------------------------A-------------------------')
    for n in (2, 4):
        y = []
        x = -2
        h = 6 / n
        for i in range(n + 1):
            y.append(f(x))
            x += h

        trapezoidal_integral = TrapezoidalIntegral(y, h)
        trapezoidal_integral.calc_integral()
        print(f'I≈{trapezoidal_integral.result}, n={n} (Trapezoidal)')

        simpson_integral = SimpsonIntegral(y, h)
        simpson_integral.calc_integral()
        print(f'I≈{simpson_integral.result}, n={n} (Simpson)')


def f(x: float) -> float:
    return 1 - x - 4 * x ** 3 + 2 * x ** 5


if __name__ == '__main__':
    main()
