# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    new_string = string.lower()
    is_repeated = set()
    for letter in new_string:
        if letter in is_repeated:
            return False
        is_repeated.add(letter)
    return True
