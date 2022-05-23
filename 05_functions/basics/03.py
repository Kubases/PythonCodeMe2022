def sum_from_list(numbers):
    return sum(numbers)


def main():
    numbers = []
    while True:
        x = input("Give me number or end with 'end' -> ")
        if x == "end":
            break
        else:
            x = int(x)
            numbers.append(x)
    print(sum_from_list(numbers))


main()
