file = open("../inwokacja.txt", encoding="utf-8")
content = file.readlines()
file.close()
word = ""
for line in content:
    for char in '!,.();':
        line = line.replace(char, '')
    words = line.split()
    for w in words:
        if len(w) > len(word):
            word = w


print(word)
