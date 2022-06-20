def sum_of_natural_numbers(n):
    if n < 1:
        return 0
    return n + sum_of_natural_numbers(n - 1)


print(sum_of_natural_numbers(10))
