password = input("Podaj haslo -> ")
correct_check = 1
if len(password) < 8:
    print("Haslo jest za krotkie")
    correct_check = 0
if password.isalpha():
    print("Brakuje cyfry")
    correct_check = 0
if password.isdigit():
    print("Brakuje liter")
    correct_check = 0
if password.isupper():
    print("Wszystkie litery sa duze")
    correct_check = 0
if password.islower():
    print("Wszystkie litery sa male")
    correct_check = 0
if correct_check:
    print("Poprawne haslo")
