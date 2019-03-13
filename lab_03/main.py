X, Y, Z = 0, 1, 2


def function(x, y):
    return x**2 + y**2
    #return x + y


def create_table(f):
    start_x = float(input('Введите начало x: '))
    finish_x = float(input('Введите конец x: '))
    start_y = float(input('Введите начало y: '))
    finish_y = float(input('Введите конец y: '))
    count = int(input('Введите количество точек: '))

    table = [[], [], []]

    step_x = (finish_x - start_x) / (count - 1)
    step_y = (finish_y - start_y) / (count - 1)

    x = start_x
    while len(table[X]) < count:
        y = start_y
        table[X].append(x)
        table[Y] = []
        table_z = []
        while len(table[Y]) < count:
            z = f(x, y)
            table[Y].append(y)
            table_z.append(z)
            y += step_y
        table[Z].append(table_z)
        x += step_x

    return table


def print_table(table):
    print('{:^10}│'.format('x\\y'), end = '')
    for i in range(len(table[Y])):
        print('{:<10.3f}'.format(table[Y][i]), end = '')

    print()
    print(end = '─' * 10 + '┼')
    print('─' * (10 * len(table[Y])))

    for i in range(len(table[X])):
        print('{:<10.3f}│'.format(table[X][i]), end = '')
        for j in range(len(table[Y])):
            print('{:<10.3f}'.format(table[Z][i][j]), end = '')
        print()


def find_start(table, x, n):
    start = -1
    for i in range(len(table)):
        if table[i] >= x:
            start = i
            break

    if start == -1:
        return len(table) - n

    if i <= n // 2:
        return 0

    start -= n // 2

    if start + n >= len(table):
        start = len(table) - n

    return start


def approximation(table, x, n):
    new_table = []

    for i in range(2 * n + 1):
        new_table.append([' '] * (n + 2))

    j = 0
    for i in range(0, len(new_table), 2):
        new_table[i][0] = table[0][j]
        new_table[i][1] = table[1][j]
        j += 1

    current = 2
    for j in range(2, len(new_table[0])):
        for i in range(1, len(new_table) - 1):
            if new_table[i - 1][j - 1] != ' ' and new_table[i + 1][j - 1] != ' ':
                new_table[i][j] = (new_table[i - 1][j - 1] - new_table[i + 1][j - 1]) /\
                                  (new_table[0][0] - new_table[current][0])
        current += 2

    return new_table


def generate_polynomial(table, x):
    coeff = []
    j = 1
    for i in range(0, len(table) // 2 + 1):
        coeff.append(table[i][j])
        j += 1

    result = 0

    for i in range(len(coeff)):
        current = coeff[i]
        for j in range(i):
            current *= x - table[j * 2][0]
        result += current

    return result


def polynomial(table, x, n_x, y, n_y):
    start_x = find_start(table[X], x, n_x + 1)
    start_y = find_start(table[Y], y, n_y + 1)

    table[X] = table[X][start_x:start_x + n_x + 1]
    table[Y] = table[Y][start_y:start_y + n_y + 1]
    table[Z] = table[Z][start_x:start_x + n_x + 1]
    for i in range(len(table[Z])):
        table[Z][i] = table[Z][i][start_y:start_y + n_y + 1]

    print_table(table)

    # Для фиксированных иксов поиск игриков и интерполяция по икс
    table_x = []
    for i in range(len(table[X])):
        t = [table[Y], table[Z][i]]
        new_table = approximation(t, y, n_y)
        result = generate_polynomial(new_table, y)
        table_x.append(result)

    new_table = approximation([table[X], table_x], x, n_x)
    result = generate_polynomial(new_table, x)

    return result


def main():
    table = create_table(function)
    print()

    print_table(table)
    print()

    n_x = int(input('Введите степень полинома для x: '))
    n_y = int(input('Введите степень полинома для y: '))
    x = float(input('Введите x: '))
    y = float(input('Введите y: '))
    print()

    z = polynomial(table, x, n_x, y, n_y)
    f = function(x, y)
    print()

    print('P({:.2f}; {:.2f}) = {:.5f}'.format(x, y, z))
    print('f({:.2f}; {:.2f}) = {:.5f}'.format(x, y, f))
    print('Погрешность: {:1.3e}'.format(abs(z - f) / (f) * 100))

    return 0

if __name__ == '__main__':
    main()
