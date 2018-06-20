import math


def trapezoidal(a, b, n):

    h = float(b - a)/n
    result = 0.5*(f(a) + f(b))
    for i in range(1, n):
        result += f(a + i*h)
    result *= h
    return result


def f(x):
    return x**2/math.sqrt(x**2+4)


print(trapezoidal(-0.8, 1.4, 300))