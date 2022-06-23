def gcd(num1, num2):
    if num2 > num1:
        num1, num2 = num2, num1
    while True:
        if num1 % num2 == 0:
            return num2
        else:
            tmp_numb = num1 % num2
            num1, num2 = num2, tmp_numb


print(gcd(282, 78))
print(gcd(150, 6))
