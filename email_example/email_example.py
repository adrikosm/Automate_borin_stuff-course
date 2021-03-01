import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)

conn.ehlo()

conn.starttls()
conn.login('', '')
body = 'AEIOU'
title = 'TITLE'
msg = str(title + body)
conn.sendmail(
    'somemail@gmail.com',
    'somemail2@gmail.com',
    msg
)

conn.quit()
