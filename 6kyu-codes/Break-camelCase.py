def solution(s):
    new = ""
    for letter in s:
        if letter.isupper():
            new += f" {letter}"
        else:
            new += letter
    return new
