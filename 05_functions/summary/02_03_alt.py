def max_of_two(x, y):
    return x if x > y else y


def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))
