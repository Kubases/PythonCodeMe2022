text = """Szybko, zbudź się, szybko, wstawaj 
Szybko, szybko, stygnie kawa 
Szybko, zęby myj i ręce"""
text = text.lower().replace(',', '').replace('\n', '')
list_of_words = text.split(" ")
unique_words = set(list_of_words)

words_dict = {}
for i in unique_words:
    words_dict[i] = list_of_words.count(i)
print(words_dict)

