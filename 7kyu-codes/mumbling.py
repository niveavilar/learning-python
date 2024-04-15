# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(st):
    new_str = ""
    for i, letter in enumerate(st):
        new_str += letter.upper() + letter.lower() * i + "-"
    return new_str[:-1]
