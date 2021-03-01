import requests
from bs4 import BeautifulSoup
import pyperclip


def get_skroutz_price(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'html.parser')
    elements = soup.select(
        '.prices > div:nth-child(4) > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(3) > span:nth-child(1) > span:nth-child(2) > strong:nth-child(1)'
    )
    return elements[0].text.strip()


url = pyperclip.paste()

price = get_skroutz_price(url)
print(f'The price is {price}')
