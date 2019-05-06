def find_root(f, start, finish, eps):
    if (start > finish):
        start, finish = finish, start
    left = start
    right = finish
    left_function = f(left)
    right_function = f(right)
    while right - left >= eps:
        mid = (right + left) / 2
        mid_function = f(mid)
        if left_function * mid_function <= 0:
            right = mid
            right_function = mid_function
            continue
        left = mid
        left_function = mid_function
    return (right + left) / 2



def integral(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result



def find_p(p_start, t_start, t0, tw, m):
    f_1 = 7242 * p_start / t_start
    f_2 = integral(lambda z: (2 * z * 7242) / (t0 + (tw - t0) * z ** m),
            0, 1, 40)
    return find_root(lambda x: f_1 - f_2 * x, 3, 25, 1e-4)




def main():
    """
    result : 10.2090
    """
    p_start = 0.5
    t_start = 300
    t0 = 8000
    tw = 2000
    m = 8
    print(find_p(p_start, t_start, t0, tw, m))



if __name__ == '__main__':
    main()

