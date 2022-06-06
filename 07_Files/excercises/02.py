import os
file = input("Write global path to your file -> ")
file_stats = os.stat(file)
print(file_stats.st_size, "bytes")
