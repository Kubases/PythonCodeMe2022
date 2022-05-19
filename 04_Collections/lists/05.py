osoby = [["Dorota", "Wellman", "dziennikarka"], ["Adam", "Małysz", "sportowiec"], ["Robert", "Lewandowski", "piłkarz"], ["Krystyna", "Janda", "aktorka"]]
for i in osoby:
    print(*i)
print()
print(*(' '.join(row) for row in osoby), sep='\n') # tego lepiej nie
print()
for person in osoby:
    for index, value in enumerate(person):
        if index == 1:
            print(value, end=" | ")
        else:
            print(value, end=" ")
    print()
