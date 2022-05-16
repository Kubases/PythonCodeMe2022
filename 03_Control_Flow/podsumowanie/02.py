txt = "aBarKadabra123"

for x, char in enumerate(txt):
    if x % 2 == 0:
        print(char, end='')
print()
print(txt[::2])
