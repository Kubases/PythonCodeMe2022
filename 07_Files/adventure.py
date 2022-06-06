bag = ['compass', 'backpack', 'flashlight', 'food rations']
bag_string = "\n".join(bag)
with open('adventure.txt', 'w') as f:
    for item in bag:
        f.write(bag_string)
    f.write('\n')
