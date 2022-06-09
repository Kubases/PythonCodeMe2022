def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi


def print_bmi(bmi):
    print(f"BMI: {bmi}")
    if bmi >= 25:
        print("Nadwaga")
    elif bmi < 18.5:
        print("Niedowaga")
    else:
        print("Bmi prawidłowe")


def main():
    weight = float(input("Give me your weight -> "))
    height = float(input("Give me you height -> "))
    bmi = calculate_bmi(weight, height)
    print_bmi(bmi)


main()
