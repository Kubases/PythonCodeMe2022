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

    if number == guess:
        win = 1
        break
    elif number > guess:
        print("Liczba jest wieksza")
    elif guess > number:
        print("Liczba jest mniejsza")
print("Liczba do zgadniecia to: ", number)
if win:
    print("Gracz wygral")
else:
    print("Komputer wygral")
