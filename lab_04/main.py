import matplotlib
import matplotlib.pyplot as plt

import numpy as np

X, Y, RO = 0, 1, 2

def table_read(filename):
    file = open(filename)
    table = [[], [], []]

    for line in file:
        x, y, ro = line.split()
        x = float(x)
        y = float(y)
        ro = float(ro)
        table[X].append(x)
        table[Y].append(y)
        table[RO].append(ro)

    return table


def print_table(table):
    print('┌' + '─' * 20 + '┬' + '─' * 20 + '┬' + '─' * 20 + '┐')
    print('│{:^20}│{:^20}│{:^20}│'.format('x', 'y', 'ρ'))
    print('├' + '─' * 20 + '┼' + '─' * 20 + '┼' + '─' * 20 + '┤')

    for i in range(len(table[X])):
        print('│{:^20.4f}│{:^20.4f}│{:^20.4f}│'.format(table[X][i], table[Y][i], table[RO][i]))

    print('└' + '─' * 20 + '┴' + '─' * 20 + '┴' + '─' * 20 + '┘')


def graph_result(table, coeff, n):
    dx = 10
    if len(table) > 1:
        dx = (table[X][1] - table[X][0])

    x = np.linspace(table[X][0] - dx, table[X][-1] + dx, 100)
    y = []
    for i in x:
        tmp = 0;
        for j in range(0, n + 1):
            tmp += phi(i, j) * coeff[j]
        y.append(tmp)

    plt.plot(x, y, color = 'black')

    x1 = [a for a in table[X]]
    y1 = [a for a in table[Y]]

    plt.plot(x1, y1, 'kD', color = 'green', label = '$исходная таблица$')
    plt.grid(True)
    miny = min(min(y), min(y1))
    maxy = max(max(y), max(y1))
    dy = (maxy - miny) * 0.03
    plt.axis([table[X][0] - dx, table[X][-1] + dx, miny - dy, maxy + dy])

    plt.show()


def phi(x, k):
    return x ** k;


def get_slau(table, n):
    N = len(table[X])
    matrix = [[0 for i in range(0, n + 1)] for j in range (0, n + 1)]
    col = [0 for i in range(0, n + 1)]

    for m in range(0, n + 1):
        for i in range(0, N):
            tmp = table[RO][i] * phi(table[X][i], m)
            for k in range(0, n + 1):
                matrix[m][k] += tmp * phi(table[X][i], k)
            col[m] += tmp * table[Y][i]
    return matrix, col


def find_col(a_copy, i_col):
    n = len(a_copy)
    a = [[a_copy[i][j] for j in range(0, n)] for i in range (0, n)]
    col = [0 for i in range(0, n)]
    for i in range(0, n):
        a[i].append(float(i == i_col))
    for i in range(0, n):
        if a[i][i] == 0:
            for j in range(i + 1, n):
                if a[j][j] != 0:
                    a[i], a[j] = a[j], a[i]
        for j in range(i + 1, n):
            d = - a[j][i] / a[i][i]
            for k in range(0, n + 1):
                a[j][k] += d * a[i][k]
    for i in range(n - 1, -1, -1):
        res = 0
        for j in range(0, n):
            res += a[i][j] * col[j]
        col[i] = (a[i][n] - res) / a[i][i]
    return col


def get_inverse(matrix):
    n = len(matrix)
    res = [[0 for i in range(0, n)] for j in range (0, n)]

    for i in range(0, n):
        col = find_col(matrix, i)
        for j in range(0, n):
            res[j][i] = col[j];
    return res;


def mult(col, b):
    n = len(col)
    new_col = [0 for j in range(0, n)]
    for j in range(0, n):
        for k in range(0, n):
            new_col[j] += col[k] * b[j][k]
    return new_col


def get_aprox(table, n):
    slau, free = get_slau(table, n)
    inverse_slau = get_inverse(slau)
    coeff = mult(free, inverse_slau)
    return coeff


def main():
    filename = input('Введите название файла: ')
    table = table_read(filename)
    print_table(table)
    n = int(input('Введите степень полинома: '))

    coeff = get_aprox(table, n)
    graph_result(table, coeff, n)

    return 0

if __name__ == '__main__':
    main()
