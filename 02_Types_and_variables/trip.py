distance = int(input("Distance(in kilometers) ->"))
mileage = float(input("mileage/100km ->"))
price = float(input("price ->"))
multiplier = distance / 100
result = multiplier * mileage * price
print(round(result, 2), 'PLN')
