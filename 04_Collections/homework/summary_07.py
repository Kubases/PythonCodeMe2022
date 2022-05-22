example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
example_list = list(set(example_list))
max_num = example_list[0]
min_num = example_list[0]
for x in example_list:
    if x > max_num:
        max_num = x
    if x < min_num:
        min_num = x
print(f"Max: {max_num}, Min: {min_num}")