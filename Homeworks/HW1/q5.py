from lib import PolyEval


def main():
    poly_eval = PolyEval([-2.2, 2, -4, 1], PolyEval.FLOOR, 3)
    print(f"FLOOR: {poly_eval.evaluate_horner(2.41)}")
    poly_eval = PolyEval([-2.2, 2, -4, 1], PolyEval.ROUND, 3)
    print(f"ROUND: {poly_eval.evaluate_horner(2.41)}")
    poly_eval = PolyEval([-2.2, 2, -4, 1], PolyEval.NO_ROUND, 3)
    print(f"NO_ROUND: {poly_eval.evaluate_horner(2.41)}")


if __name__ == '__main__':
    main()
