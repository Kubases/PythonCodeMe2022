numbers = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
lenght = int(len(numbers) / 3)
num1 = numbers[:lenght]
num2 = numbers[lenght:2 * lenght]
num3 = numbers[2 * lenght: 3 * lenght]
print(num1[::-1])
print(num2[::-1])
print(num3[::-1])
