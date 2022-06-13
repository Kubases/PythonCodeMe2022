def main():
    my_list = ['a', 'abc', 5, 5.0, [5, 3], (1, 3), 0, True, None, {}]
    for i in my_list:
        try:
            print(10 / i)
        except TypeError as err:
            print("TypeError: ", err)
        except ZeroDivisionError as err:
            print("ZeroDivisionError: ", err)


main()
