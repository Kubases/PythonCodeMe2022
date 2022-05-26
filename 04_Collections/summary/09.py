user1 = input("Podaj 4 przedmioty szkolne: ")
user2 = input("Podaj 4 przedmioty szkolne: ")
user3 = input("Podaj 4 przedmioty szkolne: ")
user4 = input("Podaj 4 przedmioty szkolne: ")
user5 = input("Podaj 4 przedmioty szkolne: ")
general_list = list()
user1 = user1.replace(',', '').lower()
general_list.append(user1.split())
user2 = user2.replace(',', '').lower()
general_list.append(user2.split())
user3 = user3.replace(',', '').lower()
general_list.append(user3.split())
user4 = user4.replace(',', '').lower()
general_list.append(user4.split())
user5 = user5.replace(',', '').lower()
general_list.append(user5.split())

general_dict = dict()

for x in general_list:
    for y in x:
        if y in general_dict:
            general_dict[y] += 1
        else:
            general_dict[y] = 1

print(general_dict)
