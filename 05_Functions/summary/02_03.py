def minimum_of(a, b, c):
    if a > b:
        if b > c:
            print(c)
        else:
            print(b)
    elif b > c:
        if c > a:
            print(a)
        else:
            print(c)
    elif c > a:
        if a > b:
            print(b)
        else:
            print(a)


def maximum_of(a, b, c):
    if a > b:
        if c > a:
            print(c)
        else:
            print(a)
    elif b > a:
        if c > b:
            print(c)
        else:
            print(b)
    elif c > a:
        if b > c:
            print(b)
        else:
            print(c)


def main():
    a = float(input("Input a number -> "))
    b = float(input("Input a number -> "))
    c = float(input("Input a number -> "))
    minimum_of(a, b, c)
    maximum_of(a, b, c)


main()
