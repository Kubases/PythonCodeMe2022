def main():
    text = input("Write Your numbers -> ")
    text = text.replace(',', '')
    num_list = text.split()
    try:
        sum_num = 0
        for number in num_list:
            number = float(number)
            sum_num += number
        print(sum_num / len(num_list))
    except ValueError:
        with open('error_types.txt', 'a') as f:
            f.write('ValueError')


if __name__ == '__main__':
    main()
