import first
import second

def main():
    p_start = float(input('P начальное: '))
    t_start = int(input('T начальное: '))
    t0 = int(input('T0: '))
    tw = int(input('Tw: '))
    m = int(input('m: '))
    print('1 часть: ', end = '')
    print(first.find_p(p_start, t_start, t0, tw, m))
    print('2 часть: ', end = '')
    print(second.find_p(p_start, t_start, t0, tw, m))

if __name__ == '__main__':
    main()

