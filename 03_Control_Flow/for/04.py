N = int(input("Podaj liczbe -> "))
while not 0 < N < 8:
    print("podana zla liczba")
    N = int(input("Podaj liczbe -> "))

suma = 1
print(N, end="! = ")

for x in range(N + 1):
    if x != 0:
        suma *= x
        if x == N:
            print(x, " = ", suma)
        else:
            print(x, end=' * ')
