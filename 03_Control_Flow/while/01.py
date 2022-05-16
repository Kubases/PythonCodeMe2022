F = 0
while F < 201:
    C = 5 / 9 * (F - 32)
    print(F, "F = ", round(C, 2), "C")
    F += 20
print("-----------------------")
for x in range(0, 201, 20):
    y = 5 / 9 * (x - 32)
    print(x, "F = ", round(y, 2), "C")
