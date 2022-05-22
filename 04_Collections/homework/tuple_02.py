numbers = (1, 2, 15, 3, 1, 2, 1, 3, 4, 5, 67, 8, 4, 1, 2, 3, 4, 1, 2, 4, 5, 2, 15)
checked = set()
print(type(checked))
for x in numbers:
    for i in range(len(numbers) - 1):
        if x == i + 1:
            print("Powtarza się")
            checked.add(x)
print("Powtarzajace sie liczby to: ", checked)
