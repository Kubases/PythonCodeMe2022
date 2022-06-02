def max_of_two(x, y):
    return x if x > y else y


def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))


def min_of_two(x, y):
    return x if x < y else y


def min_of_three(x, y, z):
    return min_of_two(x, min_of_two(y, z))


def main():
    print(min_of_three(1, 2, 3))
    print(max_of_three(1, 2, 3))

    
main()
