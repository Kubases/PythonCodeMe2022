# zadanie 2
game = 1
my_number = 17
number_of_guesses = 0
while game:
    guess = int(input("Zgadnij liczbe -> ")) % 20
    if guess == my_number:
        number_of_guesses += 1
        print(f"Congratz! You guessed in {number_of_guesses}")
        game = 0
        break
    if guess > my_number:
        print("My number is lower")
        number_of_guesses += 1
    if guess < my_number:
        print("My number is higher")
        number_of_guesses += 1
