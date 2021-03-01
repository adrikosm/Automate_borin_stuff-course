import pyperclip
import re

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
(
((\d\d\d)| ( \ (\d\d\d)))? #area code(optional)
(\s|-)                     #first separator
\d\d\d                     #first 3 digits
-                          #separator
\d\d\d\d                   #last 4 digits
(((ext(\.)?\s)|x)           #extension word part (optional)
(\d{2,5}))?                  #extension number part
)
''', re.VERBOSE)

# create a regex for email adress
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+          #name part
@                        #@ symbol
[a-zA-Z0-9_.+]+          #domain name part

''', re.VERBOSE)

# get the text off the clipboard
user_text = pyperclip.paste()

# extract the email/phone from user text
extracted_phone_numbers = phoneRegex.findall(user_text)
extracted_email_addresses = emailRegex.findall(user_text)

# clean up extracted phone numbers by converting into all_phone_numbers
allPhoneNumbers = []
for phone_number in extracted_phone_numbers:
    allPhoneNumbers.append(phone_number[0])

all_mail = []
for mail in extracted_email_addresses:
    all_mail.append(mail)

for i in range(len(allPhoneNumbers)):
    print(f'PHONE:{allPhoneNumbers[i]} EMAIL:{all_mail[i]}')

# clean up results
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extracted_email_addresses)
# print(results)
