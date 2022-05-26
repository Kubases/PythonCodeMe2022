import random
number = random.randint(1, 100)
num_of_rounds = 6
win = 0
for i in range(num_of_rounds):
    guess = 0
    guess_not_in_range = 1

    while guess_not_in_range:
        guess = int(input("Podaj liczbe w zakresie 1 do 100 -> "))
        if 1 <= guess <= 100:
            guess_not_in_range = 0
            break
        else:
            print("Podano liczbe spoza zakresu")
    dif = abs(number - guess)
    if guess == number:
        win = 1
        break
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

print("Liczba do zgadniecia to: ", number)
if win:
    print("Gracz wygral")
else:
    print("Komputer wygral")
