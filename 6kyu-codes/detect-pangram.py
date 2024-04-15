# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).

def is_pangram(s):
    letters = set()
    s = s.lower()
    for character in s:
        if character.isalpha():
            letters.add(character)
    return len(letters) == 26
