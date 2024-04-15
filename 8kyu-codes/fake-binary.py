# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.

def fake_bin(x):
    mapping_table = str.maketrans("0123456789", "0000011111")
    output_string = x.translate(mapping_table)

    return output_string
