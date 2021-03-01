import pprint

message = 'It was a bright day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)  # pretty print
pprint_to_string = pprint.pformat(count)  # transform into string
'''
---CAT EXAMPLE---
my_cat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
}

print(f'CAT KEYS: {list(my_cat.keys())}')
print(f'CAT VALUES: {list(my_cat.values())}')
print(F'CAT ITEMS: {list(my_cat.items())}')

print(f'my cat before {my_cat}')
my_cat['size'] = 'thin'
my_cat['disposition'] = 'quiet'
print(f'my cat after exercise {my_cat}')
'''
