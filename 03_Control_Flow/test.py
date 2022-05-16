pa = ""
magic = 'hokuspokus'

for num in range(0, len(magic), 2):
    pa = pa + str(num) + magic[num]
    print(pa)
