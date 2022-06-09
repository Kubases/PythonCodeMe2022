from max_of_three import max_of_three


def get_three_values():
    v1 = int(input("Write your 1st number"))
    v2 = int(input("Write your 2nd number"))
    v3 = int(input("Write your 3rd number"))
    return v1, v2, v3


def main():
    v1, v2, v3 = get_three_values()
    print(max_of_three(v1, v2, v3))


if __name__ == '__main__':
    main()
