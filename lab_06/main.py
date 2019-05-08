def function(x):
    return x / (2 + 3 * x)



def derivative(x):
    return 2 / (2 + 3 * x) ** 2



def create_table(f):
    print("Построение таблицы:")
    start = float(input("Введите начальное значение x: "))
    finish = float(input("Введите конечное значение x: "))
    count = int(input("Введите количество точек: "))

    step = (finish - start) / (count - 1)
    table = [[],[]]

    while start <= finish:
        table[0].append(start)
        table[1].append(f(start))
        start += step
    return table



def add_derivative(f, table):
    der = []
    for x in table[0]:
        der.append(f(x))
    table.append(der)
    return table



def add_oneside(table):
    oneside = ['----']
    h = table[0][1] - table[0][0]
    for i in range(1, len(table[0])):
        oneside.append((table[1][i] - table[1][i - 1]) / h)
    table.append(oneside)
    return table



def add_edge(table):
    h = table[0][1] - table[0][0]
    edge = [(-3 * table[1][0] + 4 * table[1][1] - table[1][2]) / (2 * h)]
    for i in range(1, len(table[0]) - 1):
        edge.append('----')
    n = len(table[0])
    edge.append((3 * table[1][n - 1] - 4 * table[1][n - 2] + table[1][n - 3]) / (2 * h))
    table.append(edge)
    return table



def add_central(table):
    h = table[0][1] - table[0][0]
    central = ['----']
    for i in range(1, len(table[0]) - 1):
        central.append((table[1][i + 1] - table[1][i - 1]) / (2 * h))
    central.append('----')
    table.append(central)
    return table



def add_Rynge(table):
    p = 1
    h = table[0][1] - table[0][0]
    rynge = ['----', '----']
    for i in range(2, len(table[0])):
        rynge.append(
                (table[1][i] - table[1][i - 1]) / h +\
                (((table[1][i] - table[1][i - 1]) / h) -\
                ((table[1][i] - table[1][i - 2]) / (2 * h))) / \
                (2 ** p - 1)
                )
    table.append(rynge)
    return table



def add_var(table):
    var = []
    a0 = 1
    a1 = 2
    a2 = 3
    for i in range(len(table[0])):
        if table[0][i] == 0:
            var.append('----')
        else:
            var.append(table[1][i] / table[0][i] * (a1 / (a1 + a2 * table[0][i])))
    table.append(var)
    return table



def print_table(table):
    print('┌' + '─' * 10, end = '')
    for i in range(len(table) - 2):
        print('┬' + '─' * 10, end = '')
    print('┬' + '─' * 10 + '┐')

    print('│{:^10}'.format('x'), end = '')
    print('│{:^10}'.format('y'), end = '')
    print('│{:^10}'.format("y'"), end = '')
    print('│{:^10}'.format("left"), end = '')
    print('│{:^10}'.format('edge'), end = '')
    print('│{:^10}'.format('central'), end = '')
    print('│{:^10}'.format('Rynge'), end = '')
    print('│{:^10}│'.format('var'))

    print('├' + '─' * 10, end = '')
    for i in range(len(table) - 2):
        print('┼' + '─' * 10, end = '')
    print('┼' + '─' * 10 + '┤')

    for i in range(len(table[0])):
        print('│{:^10.4f}'.format(table[0][i]), end = '')
        print('│{:^10.4f}'.format(table[1][i]), end = '')
        print('│{:^10.4f}'.format(table[2][i]), end = '')
        if table[3][i] == '----':
            print('│{:^10}'.format(table[3][i]), end = '')
        else:
            print('│{:^10.4f}'.format(table[3][i]), end = '')
        if table[4][i] == '----':
            print('│{:^10}'.format(table[4][i]), end = '')
        else:
            print('│{:^10.4f}'.format(table[4][i]), end = '')
        if table[5][i] == '----':
            print('│{:^10}'.format(table[5][i]), end = '')
        else:
            print('│{:^10.4f}'.format(table[5][i]), end = '')
        if table[6][i] == '----':
            print('│{:^10}'.format(table[6][i]), end = '')
        else:
            print('│{:^10.4f}'.format(table[6][i]), end = '')
        if table[7][i] == '----':
            print('│{:^10}'.format(table[7][i]), end = '')
        else:
            print('│{:^10.4f}'.format(table[7][i]), end = '')
        print('│')


    print('└' + '─' * 10, end = '')
    for i in range(len(table) - 2):
        print('┴' + '─' * 10, end = '')
    print('┴' + '─' * 10 + '┘')



def main():
    table = create_table(function)
    table = add_derivative(derivative, table)
    table = add_oneside(table)
    table = add_edge(table)
    table = add_central(table)
    table = add_Rynge(table)
    table = add_var(table)
    print_table(table)
    return 0



if __name__ == '__main__':
    main()

