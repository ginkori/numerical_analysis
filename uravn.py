import math


# Функция
def f(x):
    return x**3 - 0.2*x**2 + 0.3*x - 1.2


# Первая производная
def df(x):
    return 3*x**2 - 2*0.2*x + 0.3


# Вторая производная
def d2f(x):
    return 3*2*x - 2*0.2


# Метод Ньютона
def nuton(a, b, eps):
    # Если порядок границ отрезка ввели неправильный
    if a > b:
        xn = a
        a = b
        b = xn
    try:
        # Если корней на отрезке нет - выходим
        if f(a) * f(b) > 0:
            raise AssertionError()
        # Выбираем неподвижный конец отрезка, начальную точку
        if f(a) * d2f(a) > 0:
            xn = a
        else:
            xn = b
        # Первое приближение
        xn1 = xn - f(xn)/df(xn)
        i = 1
        print('{0}-th iteration = {1}'.format(i, xn1))
        # Пока не достигнута нужная точность, считаем следующее приближение
        while math.fabs(xn1 - xn) > eps:
            xn = xn1
            xn1 = xn - f(xn)/df(xn)
            i += 1
            print('{0}-th iteration = {1}'.format(i, xn1))
        return xn1
    except AssertionError:
        print("No roots in this interval.")


# Метод половинного деления
def dihotomia(a, b, eps):
    if a > b:
        xn = a
        a = b
        b = xn
    try:
        # Если корней на отрезке нет - выходим
        if f(a) * f(b) > 0:
            raise AssertionError()
        # Первое приближение
        xn = (a + b)/2
        i = 1
        print('{0}-th iteration = {1}'.format(i, xn))
        # Делим пополам, пока не достигнута нужная точность
        while math.fabs(b - a) > eps:
            # Если равно нулю, значит корень уже найден - выходим
            if f(xn) == 0:
                break
            # Выбираем и берем ту половину отрезка,
            # на концах которого значения имеют разные знаки
            if f(xn) * f(a) < 0:
                b = xn
            elif f(xn) * f(b) < 0:
                a = xn
            xn = (a + b)/2
            i += 1
            print('{0}-th iteration = {1}'.format(i, xn))
        return xn
    except AssertionError:
        print("No roots in this interval.")


# Метод секущих
def hord(a, b, eps):
    # Если порядок границ отрезка ввели неправильный
    if a > b:
        x0 = a
        a = b
        b = x0
    try:
        # Если корней на отрезке нет - выходим
        if f(a) * f(b) > 0:
            raise AssertionError()
        # Первое приближение
        xn = a - (f(a)/(f(b) - f(a))*(b - a))
        i = 1
        print('{0}-th iteration = {1}'.format(i, xn))
        # Выбираем неподвижный конец отрезка
        # Считаем приближение по нужной формуле
        if f(a) * d2f(a) > 0:
            x0 = a
            xn1 = xn - (f(xn)/(f(xn)-f(x0))*(xn - x0))
            i += 1
            print('{0}-th iteration = {1}'.format(i, xn1))
            while math.fabs(xn1 - xn) > eps:
                x0 = xn
                xn = xn1
                xn1 = xn - (f(xn)/(f(xn)-f(x0))*(xn - x0))
                i += 1
                print('{0}-th iteration = {1}'.format(i, xn1))
        else:
            x0 = b
            xn1 = xn - (f(xn)/(f(x0) - f(xn))*(x0 - xn))
            i += 1
            print('{0}-th iteration = {1}'.format(i, xn1))
            while math.fabs(xn1 - xn) > eps:
                x0 = xn
                xn = xn1
                xn1 = xn - (f(xn)/(f(x0) - f(xn))*(x0 - xn))
                i += 1
                print('{0}-th iteration = {1}'.format(i, xn1))
        return xn1
    except AssertionError:
        print("No roots in this interval.")


# Комбинированный метод
def combo(a, b, eps):
    # Если порядок границ отрезка ввели неправильный
    if a > b:
        x0 = a
        a = b
        b = x0
    try:
        # Если корней на отрезке нет - выходим
        if f(a) * f(b) > 0:
            raise AssertionError()

        # Первое приближение для хорды
        h_xn = a - (f(a)/(f(b) - f(a))*(b - a))
        i = 0
        print('{0}-th iteration horda = {1}'.format(i, h_xn))

        # Выбираем неподвижный конец отрезка
        # Считаем приближение по нужной формуле
        if f(a) * d2f(a) > 0:
            # Первое приближение для касательных, тут важно, какой конец неподвижен
            k_xn = a
            k_xn1 = k_xn - f(k_xn) / df(k_xn)
            # Второе приближение для хорды, для первого неподвижность была не важна
            h_x0 = a
            h_xn1 = h_xn - (f(h_xn)/(f(h_xn)-f(h_x0))*(h_xn - h_x0))

            i += 1
            print('{0}-th iteration:\nhorda = {1}\nkasat = {2}'.format(i, h_xn1, k_xn1))

            while math.fabs(h_xn1 - k_xn1) > eps:
                k_xn = k_xn1
                k_xn1 = k_xn - f(k_xn) / df(k_xn)

                h_x0 = h_xn
                h_xn = h_xn1
                h_xn1 = h_xn - (f(h_xn)/(f(h_xn)-f(h_x0))*(h_xn - h_x0))

                i += 1
                print('{0}-th iteration:\nhorda = {1}\nkasat = {2}'.format(i, h_xn1, k_xn1))
        else:
            # Первое приближение для касательных, тут важно, какой конец неподвижен
            k_xn = b
            k_xn1 = k_xn - f(k_xn) / df(k_xn)
            # Второе приближение для хорды
            h_x0 = b
            h_xn1 = h_xn - (f(h_xn)/(f(h_x0) - f(h_xn))*(h_x0 - h_xn))

            i += 1
            print('{0}-th iteration:\nhorda = {1}\nkasat = {2}'.format(i, h_xn1, k_xn1))

            while math.fabs(h_xn1 - k_xn1) > eps:
                k_xn = k_xn1
                k_xn1 = k_xn - f(k_xn) / df(k_xn)

                h_x0 = h_xn
                h_xn = h_xn1
                h_xn1 = h_xn - (f(h_xn)/(f(h_x0) - f(h_xn))*(h_x0 - h_xn))
                i += 1

                print('{0}-th iteration:\nhorda = {1}\nkasat = {2}'.format(i, h_xn1, k_xn1))

        return (h_xn1 + k_xn1)/2
    except AssertionError:
        print("No roots in this interval.")


# Метод итераций
def iter(a, b, eps):
    # Если порядок границ отрезка ввели неправильный
    if a > b:
        x0 = a
        a = b
        b = x0
    try:
        # Если корней на отрезке нет - выходим
        if f(a) * f(b) > 0:
            raise AssertionError()
        # Первое приближение
        x0 = a
        x = x0 - (1/df(x0))*f(x0)
        i = 1
        print('{0}-th iteration = {1}'.format(i, x))
        while math.fabs(x0 - x) > eps:
            x0 = x
            # Приводим функцию к виду x = ф(x), чтоб сходилось:
            # ф(x) = x - альфа*f(x), альфа = 1/f'(x)
            x = x - (1/df(x))*f(x)
            i += 1
            print('{0}-th iteration = {1}'.format(i, x))
        return x
    except AssertionError:
        print("No roots in this interval.")


vert_a = 1  # float(input('Input [a;'))
vert_b = 2  # float(input('Input ;b]'))
epsilon = 10**-6

print('Половинного деления Root = {0:6f}\n'.format(dihotomia(vert_a, vert_b, epsilon)))
print('Метода хорд Root = {0:6f}\n'.format(hord(vert_a, vert_b, epsilon)))
print('Метода Ньютона Root = {0:6f}\n'.format(nuton(vert_a, vert_b, epsilon)))
print('Комбинированного метода Root = {0:6f}\n'.format(combo(vert_a, vert_b, epsilon)))
print('Метода итерации Root = {0:6f}\n'.format(iter(vert_a, vert_b, epsilon)))
