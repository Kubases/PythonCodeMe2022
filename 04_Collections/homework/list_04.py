x = 1
while x % 2 != 0:
    x = int(input("Ile liczb? -> "))
numbers = []
for i in range(x):
    numbers.append(int(input("Podaj liczbe -> ")))
len_of_list = int(len(numbers) / 2)
if numbers[len_of_list] == numbers[len_of_list - 1]:
    print("Srodkowe elementy sa takie same")
else:
    print("Srodkowe elementy nie sa takie same")