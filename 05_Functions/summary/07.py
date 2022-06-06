def is_c_number(c_number):
    return c_number.isdigit() and 13 <= len(c_number) <= 16


def is_mastercard(c_number):
    return len(c_number) == 16 and (51 <= int(c_number[:2]) <= 55 or int(c_number[:4] in range(2221, 2720 + 1)))


def is_visa(c_number):
    return len(c_number) in [13, 16] and c_number[0] == '4'


def is_american_express(c_number):
    return len(c_number) == 15 and (c_number.startswith('34', '37'))


def c_type_check(c_number):
    if is_visa(c_number):
        return 'Visa'
    if is_mastercard(c_number):
        return 'Mastercard'
    if is_american_express(c_number):
        return 'American Express'


def main():
    c_number = None
    while True:
        c_number = input("Write your card number -> ").replace(" ", "")
        if is_c_number(c_number):
            print("Card number is correct")
            break
        print("Card number is not correct")

    card_type = c_type_check(c_number)
    print(f"Your card type is {card_type}")


main()
