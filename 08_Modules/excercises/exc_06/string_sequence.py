def get_stats(text):
    count = 0
    stats = list()
    for index, letter in enumerate(text):
        if index == 0:
            seq_letter = letter
            count = 1
            continue
        if letter == seq_letter:
            count += 1
        else:
            stats.append((seq_letter, count))
            seq_letter = letter
            count = 1
        if index == len(text) - 1:
            stats.append((seq_letter, count))
    return stats


def find_longest_sequence(stats):
    biggest = stats[0]
    for pair in stats:
        if pair[1] > biggest[1]:
            biggest = pair
    return biggest


def get_sequence(text):
    stats = get_stats(text)
    biggest = find_longest_sequence(stats)
    print(biggest[0] * biggest[1], biggest[1])
