import numpy as np

ITERATION_LIMIT = 1000

# Матрица констант
A = np.array([[0.07, -0.08, 0.11, -0.18],
              [0.18, 0.52, 0.0, 0.21],
              [0.13, 0.31, 0.0, -0.21],
              [0.08, -0.0, -0.33, 0.28]])
# Вектор свободных элементов
b = np.array([-0.51, 1.17, -1.02, -0.28])

# Вывод слау
print("System:")
for i in range(A.shape[0]):
    row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    row1 = "x{} =".format(i+1)
    print(row1, " + ".join(row), b[i])
print()

# Подсчет норм и проверка на сходимость
norm_1 = np.linalg.norm(A, 1)
norm_2 = np.linalg.norm(A, np.inf)
norm_3 = np.linalg.norm(A, 'fro')

if norm_1 < 1 or norm_2 < 1 or norm_3 < 1:

    x = np.zeros_like(b)
    for it_count in range(ITERATION_LIMIT):
        print("Current solution:", x)
        x_new = np.zeros_like(x)

        for i in range(A.shape[0]):
            su = np.dot(A[i], x[:])
            x_new[i] = b[i] + su

        # Принцип Рунге - точность = 10**-5
        if np.allclose(x, x_new, atol=1e-5, rtol=0.):
            break

        x = x_new

    print("Solution:")
    print(x)

else:
    print('The iteration process does not converge.\n')
    print("1-th norm = {0}\n2-th norm = {1}\n3-th norm = {2}\n".format(norm_1, norm_2, norm_3))
