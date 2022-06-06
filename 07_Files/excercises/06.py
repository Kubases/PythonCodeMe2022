def is_c_number(c_number):
    return c_number.isdigit() and 13 <= len(c_number) <= 16


def is_mastercard(c_number):
    return len(c_number) == 16 and (51 <= int(c_number[:2]) <= 55 or int(c_number[:4] in range(2221, 2720 + 1)))


def is_visa(c_number):
    return len(c_number) in [13, 16] and c_number[0] == '4'


def is_american_express(c_number):
    return len(c_number) == 15 and (c_number.startswith(('34', '37')))


def c_type_check(c_number):
    if is_visa(c_number):
        f = open('visa_cards.txt', 'a')
        f.write(f"{c_number}\n")
        f.close()
    if is_mastercard(c_number):
        f = open('mastercard_cards.txt', 'a')
        f.write(f"{c_number}\n")
        f.close()
    if is_american_express(c_number):
        f = open('american_express_cards.txt', 'a')
        f.write(f"{c_number}\n")
        f.close()


def main():
    cards_file = open('cards.txt')
    content = cards_file.readlines()

    for i in content:
        i = i.replace("\n", "").replace(" ", "")
        print(i)
        if is_c_number(i):
            c_type_check(i)
            continue
        print(i, "card number is not correct")


main()
