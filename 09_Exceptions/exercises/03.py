def main():
    my_list = ['a', "abc", 5, 5.0, [5, 3], (1, 3), 0, True, None, {}, range(2)]
    try:
        index = int(input("Write your index -> "))
        print(1 / my_list[index])
    except TypeError as err:
        print("TypeError: ", err)
    except ZeroDivisionError as err:
        print("ZeroDivisionError: ", err)
    except IndexError as err:
        print("IndexError: ", err)
    except ValueError as err:
        print("ValueError: ", err)


if __name__ == '__main__':
    main()
