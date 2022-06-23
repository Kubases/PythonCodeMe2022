def factorial_by_iteration(n):
    numbers = 1
    for i in range(1, n + 1):
        numbers *= i
    return numbers


def factorial_by_recursion(n):
    if n == 1:
        return 1
    return n * factorial_by_recursion(n - 1)


print(factorial_by_iteration(5))
print(factorial_by_recursion(5))
