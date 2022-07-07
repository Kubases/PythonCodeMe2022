def rectangle(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Sides must be numeric')  # guard clause
    return a * b


def triangle(a, h):
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise ValueError('Sides must be numeric')
    return 0.5 * a * h


def trapeze(a, b, h):
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Sides must be numeric')
    return (a + b) * h / 2


def main():
    side_a = 5
    side_b = 6

    area_r = rectangle(side_a, side_b)
    area_t = triangle(side_a, side_b)
    print(area_r, area_t)


if __name__ == '__main__':
    main()
