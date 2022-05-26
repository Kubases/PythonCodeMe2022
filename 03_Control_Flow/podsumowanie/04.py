import random
slowa = [('kamien','nozyce'), ('papier','kamien'), ('nozyce', 'papier')]
num_of_rounds = int(input("Podaj liczbe rund -> "))

ai_wins = 0
pl_wins = 0

for i in range(num_of_rounds):

    action = input("Wybierz papier, kamien albo nożyce -> ")
    ai = random.choice(slowa)[0]
    if action == ai:
        print("Remis, gracze wybrali to samo")
        continue
    for pair in slowa:
        if action == pair[0] and ai == pair[1]:
            pl_wins += 1
            draw = 0
            print("Gracz wygral runde")
            break
        elif action == pair[1] and ai == pair[0]:
            ai_wins += 1
            draw = 0
            print("Komputer wygral runde")
            break

print()
print("-----------")
if pl_wins > ai_wins:
    print("Gracz wygrał")
elif ai_wins > pl_wins:
    print("Komputer wygral")
else:
    print("Remis")
print("-----------")
