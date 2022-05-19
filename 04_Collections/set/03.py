num1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
num2 = (3, 4, 5, 6, 5, 6, 3, 5)
num3 = num1[::2] + num2[1::2]
print(num3)
num3 = set(num3)
print(num3)