import random


def menu():
    print("Welcome: ")
    print("S - Start")
    print("P - Difficulty level")
    print("Q - Quit")


def assign_symbol(symbols, action):
    if action == 'K':
        tmp = symbols[0][0]
    if action == 'P':
        tmp = symbols[1][0]
    if action == 'N':
        tmp = symbols[2][0]
    return tmp


def correct_choice(symbols):
    while True:
        action = input()
        if action == 'K' or action == 'P' or action == 'N':
            return assign_symbol(symbols, action)
        print("Err, wrong choice")
        print_game_round()


def print_game_round():
    print("Your choice:")
    print("K - Stone")
    print("P - Paper")
    print("N - Scissors")


def print_difficulty():
    print('Difficulty level:')
    print('A - Smart')
    print('B - Stupid')


def difficulty_choice():
    while True:
        print_difficulty()
        action = input()
        if action == 'A':
            return 1
        if action == 'B':
            return 0
        print("Err, wrong choice")


def game_round(symbols):
    print_game_round()
    ai = random.choice(symbols)[0]
    action = correct_choice(symbols)
    print("Ai chose", ai)
    if action == ai:
        print("Draw")
        return
    for pair in symbols:
        if action == pair[0] and ai == pair[1]:
            print("Player won")
            break
        elif action == pair[1] and ai == pair[0]:
            print("Pc won")
            break


def main():
    symbols = [('Stone', 'Scissors'), ('Paper', 'Stone'), ('Scissors', 'Paper')]
    diff_level = 0
    while True:
        menu()
        action = input()
        if action == 'S' or action == 'Start':
            game_round(symbols)
        if action == 'P' or action == 'Difficulty level':
            diff_level = difficulty_choice()
        if action == 'Q' or action == 'Quit':
            break


main()
