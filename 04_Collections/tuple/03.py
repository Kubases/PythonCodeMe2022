numbers = (1, 2, 3, 4, 5, 6, 1, 2, 3, 3, 3, 4, 5, 5,)
num = int(input("Podaj liczbe -> "))
flag = False
for i, v in enumerate(numbers):
    if int(num) == v:
        print("znalazłem, na indeksie ", i)
        flag = 1
        break
if not flag:
    print("Nie znalazłem")

if num in numbers:
    print(numbers.index(num))
else:
    print("Nie znalazłem")
