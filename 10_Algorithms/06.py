def pascal_triangle(n):
    pyramid = list()
    for row in range(n):
        pyramid.append([])
        pyramid[row].append(1)
        if row > 0:
            for j in range(1, row):
                pyramid[row].append(pyramid[row - 1][j - 1] + pyramid[row - 1][j])
            pyramid[row].append(1)

    for row in pyramid:
        print(*row)


def main():
    pascal_triangle(int(input()))


if __name__ == '__main__':
    main()
