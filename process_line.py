
#  Author:Chunyu Miao
#  Function: Process a line of string according to the task 1 requirement: takes a line of text (string) as an argument.
# It should return a new string which removes all characters from the line that are not in
# the following set: characters in the English alphabet, space, digits, or the ‘.’ character.

# Time Tue 6 November


def process_line (line_string):
    out_str =''
    ascii_difference = ord('b') - ord('B') # the difference between the uppercase and lowercase letters in ascii code
    for c in line_string:
        if ord('A') <= ord(c) <= ord('Z'):  # when the char is A-Z
            out_str += chr(ord(c) + ascii_difference)
        elif ord('a') <= ord(c) <= ord('z'):    # when the char is 'a-z'
            out_str += c
        elif ord('0') <= ord(c) <= ord('9'):    # when the char is '0-9'
            out_str += '0'
        elif ' ' == c:
            out_str += ' '
        elif '.' == c:
            out_str += '.'
    return out_str

result = process_line('125sdxa 哈哈哈 . sdcxz aszx asw22 c3 , AZSsxWxfgTG')
print(result)








