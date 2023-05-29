from lib import SecantRoot


def main():
    print('-------------------------A-------------------------')
    secant = SecantRoot(0, 2, f, 0.01)
    secant.find_root()
    print(f"x = {[round(x, 2) for x in secant.points]}")
    print(f"f(x) = {[round(f(x), 2) for x in secant.points]}")

    print('\n-------------------------B-------------------------')

    secant = SecantRoot(0, 1, f, 0.01)
    secant.find_root()
    print(f"x = {[round(x, 2) for x in secant.points]}")
    print(f"f(x) = {[round(f(x), 2) for x in secant.points]}")
    print(f"x^2 = {[round(x ** 2, 2) for x in secant.points]}")
    print(f"x^3 = {[round(x ** 3, 2) for x in secant.points]}")
    print(f"x^4 = {[round(x ** 4, 2) for x in secant.points]}")

    print('\n--------------------------C------------------------')

    secant = SecantRoot(-2, 0, f, 0.01)
    secant.find_root()
    print(f"x = {[round(x, 2) for x in secant.points]}")
    print(f"f(x) = {[round(f(x), 2) for x in secant.points]}")

    print('\n---------------------------D-----------------------')

    secant = SecantRoot(-2, 2, f, 0.01)
    try:
        secant.find_root()
    except ZeroDivisionError:
        print("Failed to find root.")
    print(f"x = {[round(x, 2) for x in secant.points]}")
    print(f"f(x) = {[round(f(x), 2) for x in secant.points]}")


def f(x: float) -> float:
    return x ** 2 - 2


if __name__ == '__main__':
    main()
