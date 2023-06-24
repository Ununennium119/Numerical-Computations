import math

from lib import PolyEval


def main():
    factorial = list(factorial_generator(10001))

    print('(1)')
    poly_eval = PolyEval([1 for _ in range(1000001)])
    x = 0.5
    print(f'1 / (1 - {x}) \u2248 {poly_eval.evaluate_horner(x)} (with Horner\'s method)')
    print(f'1 / (1 - {x}) \u2248 {poly_eval.evaluate(x)} (without Horner\'s method)')

    print()

    print('(2)')
    poly_eval = PolyEval([0 if i % 2 == 0 else ((-1) ** ((i - 1) // 2)) / factorial[i] for i in range(10001)])
    x = math.pi / 7
    print(f'sin({x}) \u2248 {poly_eval.evaluate_horner(x)} (with Horner\'s method)')
    print(f'sin({x}) \u2248 {poly_eval.evaluate(x)} (without Horner\'s method)')

    print()

    print('(3)')
    poly_eval = PolyEval([1 / factorial[i] for i in range(101)])
    x = 12
    print(f'e^{x} \u2248 {poly_eval.evaluate_horner(x)} (with Horner\'s method)')
    print(f'e^{x} \u2248 {poly_eval.evaluate(x)} (without Horner\'s method)')

    print()

    print('(4)')
    poly_eval = PolyEval([0] + [(-1) ** (i + 1) / i for i in range(1, 101)])
    x = 2.5
    print(f'log_2(1 + {x}) \u2248 {poly_eval.evaluate_horner(x) / math.log(2)} (with Horner\'s method)')
    print(f'log_2(1 + {x}) \u2248 {poly_eval.evaluate(x) / math.log(2)} (without Horner\'s method)')


def factorial_generator(n):
    fact = 1
    for i in range(n):
        if i > 0:
            fact *= i
        yield fact


if __name__ == '__main__':
    main()
