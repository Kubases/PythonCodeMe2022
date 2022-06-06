import random


def range_check(dif):
    if dif <= 5:
        print("Parzy, parzy, jestes bardzo blisko")
    elif dif <= 10:
        print("Goraco")
    elif dif <= 20:
        print("Ciepło")
    elif dif <= 40:
        print("Zimno")
    else:
        print("Mrozi, brrr")


def guess_check():
    while True:
        guess = int(input("Podaj liczbe w zakresie 1 do 100 -> "))
        if 1 <= guess <= 100:
            break
        else:
            print("Podano liczbe spoza zakresu")
    return guess


def main():
    number = random.randint(1, 100)
    num_of_rounds = 6
    win = 0
    for i in range(num_of_rounds):
        guess = guess_check()
        dif = abs(number - guess)
        if guess == number:
            win = 1
            break
        range_check(dif)

    print("Liczba do zgadniecia to: ", number)
    if win:
        print("Gracz wygral")
    else:
        print("Komputer wygral")


main()
