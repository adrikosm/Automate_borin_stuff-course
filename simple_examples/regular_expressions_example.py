import re

message = 'Call me on 415-555-1234 tommorow or on 415-555-9999 today'

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_num_regex.findall(message)
print(mo)




""""
def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


message = 'Call me on 415-555-1234 tommorow or on 415-555-9999 today'
found_number = False
for i in range(len(message)):
    chunk = message[i:i + 12]
    if is_phone_number(chunk):
        print(f'Phone number found: {chunk}')
        found_number = True
if not found_number:
    print("Could not find any phone numbers")
"""
