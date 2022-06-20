def mail_search(user_mail, mail_list):
    for i in range(len(mail_list)):
        if user_mail == mail_list[i]:
            return True
    return False


def mail_search_simplified(user_mail, mail_list):
    if user_mail in mail_list:
        return True
    return False


def mail_search_another(user_mail, mail_list):
    return user_mail in mail_list


def main():
    mail_list = ['abc@gmail.com', 'def@gmail.com', 'ghi@gmail.com', 'jkl@gmail.com']
    user_mail = input("Write your mail -> ")
    print(mail_search(user_mail, mail_list))
    print(mail_search_simplified(user_mail, mail_list))
    print(mail_search_another(user_mail, mail_list))


if __name__ == '__main__':
    main()
