import random


def get_symbol_list():
    symbols = list()
    for i in range(10):
        symbols.append(str(i))
    return symbols


def get_string(length, symbols):
    text = ''
    rand_index = random.randrange(length)
    for i in range(length - 1):
        if i == rand_index:
            letter = random.choice(symbols)
            text = text + letter + letter
            continue
        text = text + random.choice(symbols)
    return text


def get_random_string(length):
    symbols = get_symbol_list()
    text = get_string(length, symbols)
    return text


def get_custom_string(length, symbols):
    c_symbols = list(symbols)
    text = get_string(length, c_symbols)
    return text

