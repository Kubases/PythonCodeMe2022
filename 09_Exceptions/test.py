try:
    ppl = int(input())
    result = 10 / ppl
except ZeroDivisionError:
    print("Don't divide by 0")
except TypeError:
    print("Expected number")
