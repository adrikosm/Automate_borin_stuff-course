import os
import shelve

totalSize = 0
for filename in os.listdir('..\\..\\automate_boring_Stuff'):
    if not os.path.isfile(os.path.join('..\\..\\automate_boring_Stuff', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('..\\..\\automate_boring_Stuff', filename))

print(os.getcwd())

print(f'total size of files in automate boring stuff is {totalSize}: KB')

print(os.path.exists('c:\\Windows\\system32\\calc.exe'))
print(os.path.getsize('..\\phone_and_email_scrapper.py '))

shelveFile = shelve.open('mydata')
print(shelveFile['cats'])
