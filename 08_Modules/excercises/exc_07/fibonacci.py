def get_fibonacci(n):
    if n == 0:
        return n
    if n == 1:
        return n
    fc = 0
    fn = 1
    fib_list = [fc, fn]
    count = 0
    while count < (n - 2):
        next_v = fc + fn
        fib_list.append(next_v)
        fc = fn
        fn = next_v
        count += 1

    return fib_list
