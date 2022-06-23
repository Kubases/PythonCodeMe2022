def sort_surnames(filename):
    with open(filename + '.txt') as f:
        n = int(f.readline())
        content_list = list()
        for i in range(n):
            content_list.append(f.readline())
    for row in content_list:
        row = row.replace("\n", '')
    content_list.sort()
    with open(filename + '_sorted.txt', 'w') as f:
        for row in range(n):
            f.write(content_list[row])


sort_surnames('surnames')
