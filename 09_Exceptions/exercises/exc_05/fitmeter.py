import bmi


def get_file_name(bmi_status):
    if bmi_status == "over":
        return "over.txt"
    elif bmi_status == "under":
        return "under.txt"
    elif bmi_status == "obesity":
        return "too_much.txt"
    else:
        return "regular.txt"


def get_content(file_name):
    with open(file_name) as f:
        content = f.read()
    return content


def main():
    while True:
        try:
            weight = float(input("Write your weight -> "))
            height = float(input("Write your height -> "))
        except ValueError:
            print("ValueError")
        else:
            break
    try:
        bmi_status = bmi.main(weight, height)
        file_name = get_file_name(bmi_status)
        content = get_content(file_name)
        print(content)
    except ZeroDivisionError:
        print("ZeroDivisionError")


main()
