import math

ITERATION_LIMIT = 1000


def f(x):
    return x**2/math.sqrt(x**2+4)


def trapezoidal(a, b, n):

    result_1 = 0.0
    result_2 = 0.0
    for it_count in range(ITERATION_LIMIT):
        print("{0}-th iteration: {1}".format(it_count, result_1))

        h = float(b - a)/n
        result_2 = 0.5*(f(a) + f(b))
        for i in range(1, n):
            result_2 += f(a + i*h)
        result_2 *= h

        if math.fabs(result_2 - result_1) < 10**-6:
            break
        n *= 2
        result_1 = result_2

    # Правило Рунге для получения более точного ответа
    result = result_2 + (n**2/(0.5*n**2-n**2))*(result_2 - result_1)
    print('Solution: {0}\nNumber of parts: {1}'.format(result, n))


def simpson(a, b, n):

    result_1 = 0.0
    result_2 = 0.0
    for it_count in range(ITERATION_LIMIT):
        print("{0}-th iteration: {1}".format(it_count, result_1))

        h = float(b - a)/n
        result_2 = f(a) + f(b)
        for i in range(1, n):
            if i % 2 != 0:
                result_2 += 4*f(a + i*h)
            else:
                result_2 += 2*f(a + i*h)
        result_2 *= h/3

        if math.fabs(result_2 - result_1) < 10**-6:
            break
        n *= 2
        result_1 = result_2

    # Правило Рунге для получения более точного ответа
    result = result_2 + (n**4/(0.5*n**4-n**4))*(result_2 - result_1)
    print('Solution: {0}\nNumber of parts: {1}'.format(result, n))


def gauss(a, b, n):

    if n == 4:
        t_i = [-0.86114, -0.33998, 0.33998, 0.86114]
        a_i = [0.34785, 0.65215, 0.65215, 0.34785]
    elif n == 5:
        t_i = [-0.90618, -0.53847, 0.00000, 0.53847, 0.90618]
        a_i = [0.23693, 0.47863, 0.56889, 0.47863, 0.23693]
    else:
        return print('n must be 4 or 5!')

    result = 0.0

    for i in range(0, n):
        x_i = (a + b)/2 + (b - a)/2*t_i[i]
        result += a_i[i]*f(x_i)
        print("{0}-th iteration: {1}".format(i, result))

    result *= (b - a)/2
    print('Solution: {0}\nNumber of parts: {1}'.format(result, n))


trapezoidal(-0.8, 1.4, 10)
simpson(-0.8, 1.4, 10)
gauss(-0.8, 1.4, 4)
gauss(-0.8, 1.4, 5)
