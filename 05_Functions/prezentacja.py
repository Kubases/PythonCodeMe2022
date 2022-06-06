def add_book(books):
    x = input("Podaj nazwe książki -> ")
    y = int(input("Podaj ocene książki -> "))
    tmp_list = (x, y)
    books.append(tmp_list)


def find_book(books):
    x = int(input("Podaj index książki -> "))
    if 0 < x <= len(books):
        print(books[x - 1])
    else:
        print("Nie ma książki o takim indeksie")


def main():
    books = list()
    while True:
        x = input("Wpisz opcje: dodaj, znajdz, koniec")
        if x == "dodaj":
            add_book(books)
        if x == "znajdz":
            find_book(books)
        if x == "koniec":
            break


main()
