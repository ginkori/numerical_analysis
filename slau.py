import numpy as np

ITERATION_LIMIT = 1000


def jacobi(a, b):

    x = np.zeros_like(b)

    for it_count in range(ITERATION_LIMIT):
        print("{0}-th iteration: {1}".format(it_count, x))
        x_new = np.zeros_like(x)

        for n in range(a.shape[0]):
            su = np.dot(a[n], x[:])
            x_new[n] = b[n] + su

        # Принцип Рунге - точность = 10**-5
        if np.allclose(x, x_new, atol=1e-6, rtol=0.):
            break

        x = x_new

    print("Solution:")
    print(x)


def zeidel(a, b):

    x = np.zeros_like(b)

    for it_count in range(ITERATION_LIMIT):
        print("{0}-th iteration: {1}".format(it_count, x))
        x_new = np.zeros_like(x)

        for n in range(a.shape[0]):
            s1 = np.dot(a[n, :n], x_new[:n])
            s2 = np.dot(a[n, n:], x[n:])
            x_new[n] = b[n] + s1 + s2

        if np.allclose(x, x_new, atol=1e-6, rtol=0.):
            break

        x = x_new

    print("Solution:")
    print(x)


# Матрица констант
a_matrix = np.array([[0.07, -0.08, 0.11, -0.18],
                    [0.18, 0.52, 0.0, 0.21],
                    [0.13, 0.31, 0.0, -0.21],
                    [0.08, -0.0, -0.33, 0.28]])
# Вектор свободных элементов
b_el = np.array([-0.51, 1.17, -1.02, -0.28])

# Вывод слау
print("System:")
for i in range(a_matrix.shape[0]):
    row = ["{}*x{}".format(a_matrix[i, j], j + 1)
           for j in range(a_matrix.shape[1])]
    row1 = "x{} =".format(i+1)
    print(row1, " + ".join(row), b_el[i])
print()

# Подсчет норм и проверка на сходимость
norm_1 = np.linalg.norm(a_matrix, 1)
norm_2 = np.linalg.norm(a_matrix, np.inf)
norm_3 = np.linalg.norm(a_matrix, 'fro')

if norm_1 < 1 or norm_2 < 1 or norm_3 < 1:
    jacobi(a_matrix, b_el)
    zeidel(a_matrix, b_el)
else:
    print('The iteration process does not converge.\n')
    print("1-th norm = {0}\n2-th norm = {1}\n3-th norm = {2}\n".format(norm_1, norm_2, norm_3))
