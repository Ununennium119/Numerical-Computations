from lib import PolyEval


def main():
    poly_eval = PolyEval([1, -4, 2, -2.2], PolyEval.FLOOR, 3)
    print(f"FLOOR: {poly_eval.evaluate(2.41)}")
    poly_eval = PolyEval([1, -4, 2, -2.2], PolyEval.ROUND, 3)
    print(f"ROUND: {poly_eval.evaluate(2.41)}")
    poly_eval = PolyEval([1, -4, 2, -2.2], PolyEval.NO_ROUND, 3)
    print(f"NO_ROUND: {poly_eval.evaluate(2.41)}")


if __name__ == '__main__':
    main()
