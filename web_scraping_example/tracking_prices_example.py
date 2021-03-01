import requests
from bs4 import BeautifulSoup
import smtplib


def check_price():
    URL = 'https://www.skroutz.gr/s/23272541/Xiaomi-Redmi-Note-9-Pro-64GB-Interstellar-Gray.html'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.select('#nav > h1:nth-child(5) > a:nth-child(1)')

    price = soup.select(
        '.prices > div:nth-child(4) > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(3) > span:nth-child(1) > span:nth-child(2) > strong:nth-child(1)')

    converted_price = price[0]
    converted_price = converted_price.text
    numeric_price = converted_price[:-3]

    numeric_price = numeric_price.replace(',', '.')
    print(f'{title[0].text} is priced at {converted_price}')

    if float(numeric_price) < 300:
        send_mail(URL)


def send_mail(url):
    body = f'Check the link ' + url
    print(body)

    """"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('', '')
    subject = "Price fell down"
    body = 'Check the link  ' + url
    msg = f'Subject : {subject}\n\n{body}'
    server.sendmail(
        'adrikosm@gmail.com',
        'nottrulyasaint@gmai.com',
        msg
    )
    print("EMAIL HAS BEEN SENT")
    server.quit()
"""


check_price()
