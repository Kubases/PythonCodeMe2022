def check_num_in_range(number, my_range):
    if number in my_range:
        return True
    else:
        return False


def main():
    start = int(input("Podaj poczatek przedzialu -> "))
    end = int(input("Podaj koniec przedzialu -> "))
    my_range = range(start, end)
    number = int(input("Podaj liczbe -> "))
    flag = check_num_in_range(number, my_range)
    if flag:
        print(f"tak, liczba {number} znajduje się w zadanym zakresie")
    else:
        print(f"nie, liczba {number} jest z poza zakresu")


main()
