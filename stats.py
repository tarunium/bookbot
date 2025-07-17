def count_words(text):
    total_words = 0
    words = text.split()
    total_words = len(words)
    return total_words

def count_chars(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts.update({char: 1})
    return char_counts

def split_counts(char_counts):
    count_list = []
    for char in char_counts:
        char_dict = {"char": char, "num": char_counts[char]}
        count_list.append(char_dict)
    return count_list

def sort_on(dict):
    return dict["num"]

def sort_counts(char_counts):
    count_list = split_counts(char_counts)
    count_list.sort(reverse = True, key = sort_on)
    return count_list
