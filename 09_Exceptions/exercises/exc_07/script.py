import random


def print_random_quote(content):
    line = random.choice(content)
    line = line.replace("\n", "")
    length = (len(line) + 20)
    line_list = list(line.split())
    author = ' - ' + str(line_list[-2:])
    line = line.rstrip(author)
    author = author.replace("'", '').replace("[", "").replace("]", "").replace(",", "").lstrip(" - ")
    print('*' * length)
    print(line.center(length))
    print(author.center(length))
    print('*' * length)


def main():
    while True:
        try:
            file_name = input("Write name of your file -> ")
            with open(file_name) as f:
                content = f.readlines()
        except FileNotFoundError:
            print("No file found")
        else:
            break
    print_random_quote(content)


main()
