suma = 0
N = 3
for x in range(N):
    subject = input("Podaj nazwe przedmiotu -> ")
    grade = int(input("Podaj ocene -> "))
    print(f"{subject}: {grade}")
    suma += grade
