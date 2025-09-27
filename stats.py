def get_num_words(text):
    words = text.split()
    return len(words)


def num_per_char(text):
    char_count = {}
    lowered = text.lower()
    for char in lowered:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count


def sort_on(item):
    return item["num"]


def to_list_of_dicts(char_counts):
    result = []
    for ch in char_counts:
        count = char_counts[ch]
        item = {"char": ch, "num": count}
        result.append(item)
    return result


def sorted_char_counts(char_counts):
    items = to_list_of_dicts(char_counts)
    items.sort(key=sort_on, reverse=True)
    return items
