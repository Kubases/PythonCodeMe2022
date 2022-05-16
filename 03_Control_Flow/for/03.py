liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = 0
for x in liczby:
    for i in range(x + 1):
        suma += i
    print(suma)
    suma = 0
