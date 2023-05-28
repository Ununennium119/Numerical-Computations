from lib import GradientDescent


def main():
    print("---------------------------B---------------------------")
    alpha_list = [0.001, 0.01, 0.5, 1, 2, 2.5]
    for alpha in alpha_list:
        gradient_descent = GradientDescent(
            [50, 10],
            alpha,
            [f_beta1, f_beta2],
            None,
            1000
        )
        print(f'\u03B1 = {alpha}', end=', ')
        print(f'\u03B2 = {gradient_descent.find_root()}', end=', ')
        print(f'error = {[gradient_descent.points[-2][i] - gradient_descent.points[-1][i] for i in range(2)]}')

    print("\n---------------------------C---------------------------")
    beta_list = [[100.0, 10.0], [-1000.0, 1000.0]]
    for beta in beta_list:
        gradient_descent = GradientDescent(
            beta,
            0.1,
            [f_beta1, f_beta2],
            0.001,
            1000
        )
        print(f'\u03B20 = {beta}', end=', ')
        print(f'\u03B2 = {gradient_descent.find_root()}', end=', ')
        print(f'iterations count = {gradient_descent.iterations_count}', end=', ')
        print(f'error = {[gradient_descent.points[-2][i] - gradient_descent.points[-1][i] for i in range(2)]}')


def f_beta1(beta: list[float]):
    x = [1.7, 1.7, 1.7]
    y = [80, 79, 60]
    value = 0
    for i in range(3):
        value += y[i] - beta[0] - beta[1] * x[i]
    return (-2 / 3) * value


def f_beta2(beta: list[float]):
    x = [1.7, 1.7, 1.7]
    y = [80, 79, 60]
    value = 0
    for i in range(3):
        value += (-2 * x[i]) * (y[i] - beta[0] - beta[1] * x[i])
    return value / 3


if __name__ == '__main__':
    main()
