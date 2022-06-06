f = open("text.txt")
print(f.readline())
print(f.readlines())
f.close()
with open("text.txt") as f:
    content = f.readlines()
    for line in content:
        print(line)

