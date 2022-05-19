numbers = []
for i in range(10):
    numbers.append(int(input("Podaj liczbe -> ")))
for i in numbers:
    if i % 2 != 0:
        print(i)
