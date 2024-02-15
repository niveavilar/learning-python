def find_short(s):
    words = s.split()
    small = min(words, key=len)
    l = len(small)
    return l # l: shortest word length
