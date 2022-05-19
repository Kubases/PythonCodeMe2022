n = int(input("Podaj wymiar -> "))

tab = []
for i in range(n):
    tab1 = []
    for j in range(n):
        tab1.append("-")
    tab.append(tab1)
for i in tab:
    print(*i)

tab2 = [['-'] * n] * n