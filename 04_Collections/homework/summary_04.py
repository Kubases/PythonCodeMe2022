table = list()
for x in range(10):
    tmp_list = list()
    for y in range(10):
        tmp_list.append((x + 1) * (y + 1))
    table.append(tmp_list)
for x in table:
    print(*x)

