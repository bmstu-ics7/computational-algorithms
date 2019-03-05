from math import cos, sin, pi
X = 0
Y = 1

def function(x):
    return x * x
    # return cos(90 * x / 57.2958)


def create_table(f):
    print("Построение таблицы:")
    start = float(input("Введите начальное значение x: "))
    finish = float(input("Введите конечное значение x: "))
    count = int(input("Введите количество точек: "))

    if start > finish:
        start, finish = finish, start

    step = (finish - start) / (count - 1)
    table = [[],[]]

    while start <= finish:
        table[X].append(start)
        table[Y].append(f(start))
        start += step

    return table

def create_table_file(f):
    file = open(input("Введите файл: "))
    table = [[], []]

    for line in file:
        x = float(line)
        table[X].append(x)
        table[Y].append(f(x))

    return table


def print_table(table):
    for i in range(len(table[0])):
        print("{:3}{:15.5f} {:15.5f}".format(i + 1, table[X][i], table[Y][i]))


def spline(x, table):
    N = len(table[X])

    prev_y = table[Y][1]
    prev_h = table[X][1] - table[X][0]

    next_xi = 0
    next_eta = 0

    xi, eta = [], []
    xi.append(next_xi)
    xi.append(next_xi)
    xi.append(next_xi)
    eta.append(next_eta)
    eta.append(next_eta)
    eta.append(next_eta)

    for i in range(2, N):
        current_y = table[Y][i]
        current_h = table[X][i] - table[X][i - 1]

        A = prev_h
        B = -2 * (prev_h + current_h)
        D = current_h
        F = -3 * ( (current_y - prev_y) / current_h - (prev_y - table[Y][i - 2]) / prev_h )

        current_xi, current_eta = next_xi, next_eta
        next_xi = D / (B - A * current_xi)
        next_eta = (A * current_eta + F) / (B - A * current_xi)

        xi.append(next_xi)
        eta.append(next_eta)

        prev_y = current_y
        prev_h = current_h

    c = [0] * (N + 1)
    c[N] = 0
    c[0] = 0

    #print("{:10}{:10}".format("xi", "eta"))
    #for i in range(len(xi)):
    #    print("{:<10.2f}{:<10.2f}".format(xi[i], eta[i]))

    for i in range(N - 1, 0, -1):
        c[i] = xi[i + 1] * c[i + 1] + eta[i + 1]

    a, d, b = [0], [0], [0]

    for i in range(1, N):
        a.append(table[Y][i - 1])
        h = table[X][i] - table[X][i - 1]
        d.append((c[i + 1] - c[i]) / (3 * h))
        b.append((table[Y][i] - table[Y][i - 1]) / h - h * (c[i + 1] + 2 * c[i]) / 3)

    #print("{:10}{:10}{:10}{:10}".format("a", "b", "c", "d"))
    #for i in range(len(a)):
    #    print("{:<10.2f}{:<10.2f}{:<10.2f}{:<10.2f}".format(a[i], b[i], c[i], d[i]))

    index = N - 2
    for i in range(1, N):
        if (table[X][i] > x):
            index = i - 1

    return a[index + 1] + b[index + 1] * (x - table[X][index]) + c[index + 1] * (x - table[X][index]) ** 2 + d[index + 1] * (x - table[X][index]) ** 3


def main():
    table = create_table(function)
    print_table(table)

    x = int(input("Введите x: "))

    value = spline(x, table)
    print("phi(" + str(x) + ") = " + str(value))
    print("f(" + str(x) + ") = " + str(function(x)))
    print("Погрешность метода: {:.4f}".format((function(x) - value) / function(x) * 100) )


if __name__ == '__main__':
    main()

