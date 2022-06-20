import io


def read_file():
    with open("text.txt", 'r') as f:
        pass


def read_file_in_write_mode():
    with open("abc.txt", 'w') as f:
        content = f.read()


def create_file():
    with open('abc.txt', 'x') as f:
        pass


def main():
    try:
        read_file()
    except FileNotFoundError:
        print("No file found to read")

    try:
        read_file_in_write_mode()
    except io.UnsupportedOperation:
        print("Can't read file in write mode")
    try:
        create_file()
    except FileExistsError:
        print("File already exists")


if __name__ == '__main__':
    main()
