from main import *

def f(x):
    return cos(x / 57.2958) - x


def main():
    table = create_table(f)
    print_table(table)
    print()

    table[0], table[1] = table[1], table[0]
    print_table(table)
    print()

    n = int(input("Введите степень полинома: "))
    print("x = 0\n")
    x = 0

    new_table = approximation(table, x, n)
    print_approximation(new_table)
    print()

    print(generate_polinom(new_table, x))

if __name__ == "__main__":
    main()

