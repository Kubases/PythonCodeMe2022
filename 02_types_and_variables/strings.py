txt1 = "naprawde_dlugi_text"
halved = int(len(txt1) / 2)
print(txt1[halved - 1: halved + 2])

s1 = "przykladowe"
s2 = "slowo"
half = int(len(s1) / 2)
s3 = s1[:half] + s2 + s1[half:]
print(s3)

quote = "Honesty is the first chapter in the book of wisdom."
length = len(quote)
half = int(length / 2)
print(length)
print(quote[-7:-1])
print(quote[:half + 1])
print(quote[quote.find(".")])
print(quote[half::3])
print(quote[::2])
print(quote[::-1])
print(quote.replace("wisdom", "friendship"))
