data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]

for i in data:
    print(i[0])
    print()
    for n in i[1]:
        if n % 7 == 0 and n != 0:
            print()
        if i[1][n] < 10:
            print(f"0{i[1][n]}", end=' ')
        else:
            print(i[1][n], end=' ')
    print()
    print()
