x = int(input("Podaj liczbe -> "))
squared_nums = list()
for i in range(x):
    squared_nums.append([i + 1, (i + 1) ** 2])
squared_nums = dict(squared_nums)
print(squared_nums)
