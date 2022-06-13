import sys


def cut_cake():
    parts = int(input("Write number of people -> "))
    return 10 / parts


def main():
    try:
        result = cut_cake()
    except (ZeroDivisionError, ValueError) as err:
        print("Error", err)
    else:
        print(result)
    finally:
        print('End of program')

    try:
        with open('filename.txt') as f:
            content = f.read()
    except FileNotFoundError:
        print("No file found")

    try:
        result = cut_cake()
    except Exception:
        print("Error: ", sys.exc_info()[0])


if __name__ == '__main__':
    main()
