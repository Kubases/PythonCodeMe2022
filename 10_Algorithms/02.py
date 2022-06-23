def sum_of_number(n):
    numbers = list()
    num1 = 5
    num2 = 7
    while True:
        if num1 < n:
            numbers.append(num1)
            num1 += 5
        if num2 < n:
            numbers.append(num2)
            num2 += 7
        if num1 > n or num2 > n:
            break
    return sum(numbers)


print(sum_of_number(21))
