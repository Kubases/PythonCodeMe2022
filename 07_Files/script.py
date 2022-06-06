f = open("inwokacja.txt")
content = f.readlines()

for i in content:
    print(i, end="")

f.close()
print()
print()
f = open("inwokacja.txt")
content = f.read()
print(content)
f.close()
print()
with open("inwokacja.txt") as f:
    while True:
        line = f.readline()
        print(line, end="")
        if "" == line:
            break

with open("inwokacja.txt") as f:
    content = f.readlines()

for line in content:
    print(line)
print(content)
