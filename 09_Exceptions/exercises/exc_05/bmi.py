def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi


def return_bmi(bmi):
    print(f"BMI: {bmi}")
    if bmi >= 30:
        return "obesity"
    elif bmi >= 25:
        return "over"
    elif bmi < 18.5:
        return "under"
    else:
        return "regular"


def main(weight, height):
    bmi = calculate_bmi(weight, height)
    return return_bmi(bmi)


if __name__ == '__main__':
    weight = float(input("Write your weight -> "))
    height = float(input("Write your height -> "))
    print(main(weight, height))
