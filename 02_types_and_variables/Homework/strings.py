# zadanie 2
s1 = "przykladowe"
s2 = "slowo"
half = len(s1) // 2
s3 = s1[:half] + s2 + s1[half:]
print("2: ", s3)

# zadanie 4

book_name = input("Podaj nazwe ksiazki -> ")
author_name = input("Podaj autora -> ")
num_pages = input("Podal liczbe stron -> ")
print("4.1.1: ", not book_name.isdigit())
print("4.1.2: ", not author_name.isdigit())
print("4.1.3: ", num_pages.isdigit())

book_name = book_name.capitalize()
author_name = author_name.capitalize()

all_in_one = book_name + ' ' + author_name + ' ' + num_pages
print("4.2, 4.3: ", all_in_one)

print("4.4: ", len(book_name))

# zadanie 5
txt = input()
txt = txt.lower().replace(' ', '')
print(txt == txt[::-1])

# zadanie 6
text = "Beautiful is better than ugly. " \
       "Explicit is better than implicit. " \
       "Simple is better than complex. " \
       "Complex is better than complicated. " \
       "Flat is better than nested. " \
       "Sparse is better than dense. " \
       "Readability counts. " \
       "Special cases aren't special enough to break the rules. " \
       "Although practicality beats purity. " \
       "Errors should never pass silently. " \
       "Unless explicitly silenced. " \
       "In the face of ambiguity, refuse the temptation to guess. " \
       "There should be one-- and preferably only one --obvious way to do it. " \
       "Although that way may not be obvious at first unless you're Dutch. " \
       "Now is better than never. " \
       "Although never is often better than *right* now. " \
       "If the implementation is hard to explain, it's a bad idea. " \
       "If the implementation is easy to explain, it may be a good idea. " \
       "Namespaces are one honking great idea -- let's do more of those! "
print("6.1: ", text.count("better"))
print("6.2: ", text.replace("*", ""))
print("6.3: ", text.replace("explain", "understand", 1))
print("6.4: ", text.replace(" ", "-"))

# zadanie 7
language = "Python"
adjective = "amazing"
print("{lang} is {adj}!".format(lang=language, adj=adjective))
