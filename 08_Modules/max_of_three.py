def max_of_two(x, y):
    return x if x > y else y


def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))


def start(v1, v2, v3):
    print(max_of_three(v1, v2, v3))


if __name__ == '__main__':
    start(1, 2, 3)
