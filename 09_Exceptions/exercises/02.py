def main():
    my_tup = (1, 4, 5, 7, 8, 2, 4, 6, 3, 6)
    user_value = input("Write your value -> ")
    while True:
        try:
            index = int(input("Write index -> "))
        except ValueError:
            print("ValueError")
        else:
            break
    try:
        my_tup[index] = user_value
    except TypeError:
        print("TypeError")


if __name__ == '__main__':
    main()