def main():
    with open("quotes.txt") as f:
        content = f.readlines()
    i = 0
    for line in content:
        if i > 5:
            break
        print(line)
        i += 1


main()
