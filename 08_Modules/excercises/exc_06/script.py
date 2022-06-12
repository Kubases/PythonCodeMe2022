from string_sequence import get_sequence
from string_generator import get_random_string, get_custom_string


def main():
    text1 = get_random_string(15)
    text2 = get_custom_string(10, ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    get_sequence(text1)
    get_sequence(text2)


main()
