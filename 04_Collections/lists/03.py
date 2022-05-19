x = int(input("Ile liczb? "))
numbers = []
for i in range(x):
    numbers.append(int(input("Podaj liczbe -> ")))
if numbers[0] == numbers[-1]:
    print("Pierwszy i ostatni sa takie same")
else:
    print("Pierwszy i ostatni nie sa takie same")