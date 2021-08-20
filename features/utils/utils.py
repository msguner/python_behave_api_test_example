def split_text(text, split_char=","):
    return [x.strip() for x in text.split(split_char)]


def compare_lists(list1, list2):
    return list1.sort() is list2.sort()
