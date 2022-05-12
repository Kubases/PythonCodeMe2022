txt = "2323154231251"
print(txt.isdecimal())

txt2 = "mata"
print(txt2.center(10, '*'))

txt3 = "testowy tekst"
print(txt3.removesuffix('tekst'))

txt4 = "www.flynerd.pl"
to_remove = input("type text to remove ->")
print(txt4.strip(to_remove))

txt5 = "PrzYkladOwy Tekst DO sprawdzenia"
check = 0
for i in txt5:
    if i.isupper():
        check = 1
        break
if check:
    print(txt5, ", Uppercase letter exists")
else:
    print(txt5, ", Uppercase letter doesn't exist")

answer = txt5.isalpha() and (not txt5.islower() and not txt5.isupper())
print(answer)

txt6 = "banana"
print(txt6.count('na'))