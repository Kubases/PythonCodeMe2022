def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def print_even_from_list(numbers):
    even_list = []
    for i in numbers:
        if is_even(i):
            even_list.append(i)
    print(even_list)


def main():
    numbers = [2, 3, 4, 1, 2, 3, 4, 6, 7, 3, 5, 6, 1, 4, 13, 0, 87, 6, 43]
    print_even_from_list(numbers)


main()
