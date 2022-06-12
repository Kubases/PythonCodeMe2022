from calc_delta import get_delta


def main():
    a = float(input("Write factor of x^2 -> "))
    b = float(input("Write factor of x^1 -> "))
    c = float(input("Write factor of x^0 -> "))
    delta = get_delta(b, a, c)
    print(delta)


if __name__ == '__main__':
    main()
