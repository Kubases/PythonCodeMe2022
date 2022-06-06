# zadanie 1
print(0b10100)

# zadanie 2
bin_num = 1001111
suma = 0
i = 0
while bin_num != 0:
    dec = bin_num % 10
    suma += dec * 2 ** i
    i += 1
    bin_num = bin_num // 10
print(suma)

# zadanie 3
hex_num = 0x1DB
oct_num = 0o2063
print(int(hex_num))
print(int(oct_num))
