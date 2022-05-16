weight = float(input("your weight(kg) ->"))
height = float(input("your height(m) ->"))
bmi = weight / height ** 2
print(round(bmi, 2))
if bmi < 18.5:
    print("niedowaga")
elif bmi > 25:
    print("nadwaga")
else:
    print("waga normalna")
