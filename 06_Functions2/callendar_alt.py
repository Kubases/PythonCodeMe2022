def print_month(month_name, month_days):
    print('\n', month_name)
    print()
    for i in month_days:
        if i % 7 == 0 and i != 0:
            print()
        if i < 9:
            print(f"0{i+1}", end=" ")
        else:
            print(i + 1, end=" ")
    print()


def is_transcendental(year):
    if year % 4 == 0:
        return True
    return False


def main():
    data = [
        ('January', range(31)),
        ('February', range(28)),
        ('March', range(31)),
        ('April', range(30)),
        ('May', range(31)),
        ('June', range(30)),
        ('July', range(31)),
        ('August', range(31)),
        ('September', range(30)),
        ('October', range(31)),
        ('November', range(30)),
        ('December', range(31)),
          ]
    year = int(input("What year is it? -> "))
    if is_transcendental(year):
        data[1] = ('February', range(29))
    data_dict = dict(data)

    for name, days in data_dict.items():
        print_month(name, days)


main()
