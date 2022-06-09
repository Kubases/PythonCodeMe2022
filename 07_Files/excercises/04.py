import random


def main():
    with open("quotes.txt") as f:
        quote = list()
        while True:
            current_line = f.readline()
            if current_line == "":
                break
            quote.append(current_line)
    for i in range(3):
        print(random.choice(quote))


main()
