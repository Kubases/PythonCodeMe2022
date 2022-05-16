# zadanie 1
x = int(input("Podaj liczbe -> "))
if x % 3 == 0:
    print("Twoja liczba jest podzielna przez 3")

# zadanie 2
y = int(input("Podaj pierwsza liczbe"))
z = int(input("Podaj druga liczbe"))
if y + z > 100:
    print(y + z)
else:
    print("Koniec")

# zadanie 3
op1 = int(input("Podaj opinie "))
op2 = int(input("Podaj opinie "))
op3 = int(input("Podaj opinie "))
result = (op1 + op2 + op3) / 3
if result > 7:
    print("Bardzo dobry")
elif result > 5:
    print("Przecietna")
else:
    print("Nie warta uwagi")

# zadanie 4
text = "Bardzo przykladowe zdanie"
if len(text) > 5 and text.find('a') != -1:
    print(text.replace('a', 'z'))

# zadanie 5
password = input("Podaj haslo -> ")
if len(password) < 8:
    print("haslo jest za krotkie")
elif password.isalpha():
    print("Brakuje cyfry")
elif password.isdigit():
    print("Brakuje liter")
elif password.isupper():
    print("wszystkie litery sa duze")
elif password.islower():
    print("wszystkie litery sa male")
else:
    print("Poprawne haslo")
