from bs4 import BeautifulSoup
import requests

def get_html(url):
    page = requests.get(url)
    page.raise_for_status()
    return page.text

def parse(html):
    html = get_html(html)
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('h2')
    for row in rows:
        link = row.find('a')['href']
        text = row.find('a').text
        print(text, link)
    return link, text


