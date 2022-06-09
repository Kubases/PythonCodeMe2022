from figure_areas import rectangle, square, circle


def main():
    rooms = {
        "square": [4, 5, 2],
        "circle": [3, 4, 5],
        "rectangle": [[1, 2], [3, 4]]
    }
    sum_room = 0
    for i in rooms["square"]:
        sum_room += square(i)
    for i in rooms["circle"]:
        sum_room += circle(i)
    for i in rooms["rectangle"]:
        sum_room += rectangle(i[0], i[1])
    print(sum_room)


if __name__ == '__main__':
    main()
