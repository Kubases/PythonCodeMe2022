def uppercase_decorator(param_func):
    def nested():
        text = param_func().upper()
        print(text)
        print()

    return nested


@uppercase_decorator
def return_text():
    return 'abracadabra'


def main():
    return_text()


if __name__ == '__main__':
    main()
