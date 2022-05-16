x = input("Podaj pierwsza liczbe -> ")
y = input("Podaj druga liczbe -> ")
z = input("Podaj trzecia liczbe -> ")
if x > y and x > z:
    if y > z:
        print(x, y, z)
    else:
        print(x, z, y)
if y > x and y > z:
    if x > z:
        print(y, x, z)
    else:
        print(y, z, x)
if z > x and z > y:
    if y > x:
        print(z, y, x)
    else:
        print(z, x, y)
