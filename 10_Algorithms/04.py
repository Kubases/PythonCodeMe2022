from math import floor


def bubble_sort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print(numbers)
    return numbers


def binary_search(n, numbers):
    numbers = bubble_sort(numbers)
    left = 0
    right = len(numbers) - 1
    while left <= right:
        index = floor((left + right) / 2)
        if numbers[index] < n:
            left = index + 1
        elif numbers[index] > n:
            right = index - 1
        if numbers[index] == n:
            return n
    return None


def main():
    data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
    elem = 21
    print(binary_search(elem, data))


if __name__ == '__main__':
    main()