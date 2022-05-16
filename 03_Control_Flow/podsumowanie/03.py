txt = input("Podaj dowolny ciag znakow -> ")

small_count = 0
big_count = 0
digit_count = 0
special_count = 0
for x in txt:
    if x.islower():
        small_count += 1
        continue
    if x.isdigit():
        digit_count += 1
        continue
    if x.isupper():
        big_count += 1
        continue
    if not x.isalpha() and not x.isdigit():
        special_count += 1
print("Małych lioter jest: ", small_count)
print("Dużych liter jest: ", big_count)
print("Cyfr jest: ", digit_count)
print("Znakow specjalnych jest: ", special_count)

