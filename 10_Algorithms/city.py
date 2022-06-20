def return_place(number):
    match number:
        case 0:
            return 'house'
        case 1:
            return 'school'
        case 2:
            return 'church'
        case 3:
            return 'bar'
        case 4:
            return 'hospital'
        case 5:
            return 'cinema'
        case 6:
            return 'theatre'


def main():
    routes_list = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 4), (2, 0), (2, 3), (2, 5), (3, 0), (3, 2), (3, 4), (4, 1),
                   (4, 3), (4, 6), (5, 2), (5, 4), (5, 6)]
    for i in routes_list:
        text = '' + return_place(i[0]) + ' --> ' + return_place(i[1])
        print(text)


main()
