from file_opener import open_file, write_file


def main():
    content = open_file("text.txt")
    print(content)

    text_to_save = "abcde\n21421"
    write_file('test.txt', text_to_save)


main()
