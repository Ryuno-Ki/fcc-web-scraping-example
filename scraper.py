from os import path
from pathlib import PurePath
from unittest import TestCase

from bs4 import BeautifulSoup
import requests

urls = [
  'https://www.gesetze-im-internet.de/gg/art_1.html',
  'https://www.gesetze-im-internet.de/gg/art_2.html',
  'https://www.gesetze-im-internet.de/gg/art_3.html',
  'https://www.gesetze-im-internet.de/gg/art_4.html',
  'https://www.gesetze-im-internet.de/gg/art_5.html',
  'https://www.gesetze-im-internet.de/gg/art_6.html',
  'https://www.gesetze-im-internet.de/gg/art_7.html',
  'https://www.gesetze-im-internet.de/gg/art_8.html',
  'https://www.gesetze-im-internet.de/gg/art_9.html',
  'https://www.gesetze-im-internet.de/gg/art_10.html',
  'https://www.gesetze-im-internet.de/gg/art_11.html',
  'https://www.gesetze-im-internet.de/gg/art_12.html',
  'https://www.gesetze-im-internet.de/gg/art_12a.html',
  'https://www.gesetze-im-internet.de/gg/art_13.html',
  'https://www.gesetze-im-internet.de/gg/art_14.html',
  'https://www.gesetze-im-internet.de/gg/art_15.html',
  'https://www.gesetze-im-internet.de/gg/art_16.html',
  'https://www.gesetze-im-internet.de/gg/art_16a.html'
  'https://www.gesetze-im-internet.de/gg/art_17.html',
  'https://www.gesetze-im-internet.de/gg/art_17a.html',
  'https://www.gesetze-im-internet.de/gg/art_18.html',
  'https://www.gesetze-im-internet.de/gg/art_19.html'
]


def download_urls(urls, dir):
    paths = []

    for url in urls:
        file_name = PurePath(url).name
        file_path = path.join(dir, file_name)
        text = ''

        try:
            response = requests.get(url)
            if response.ok:
                text = response.text
        except requests.exceptions.ConnectionError as exc:
            print(exc)
    
        with open(file_path, 'w') as fh:
            fh.write(text)

        paths.append(file_path)

    return paths

def parse_html(paths):
    with open(paths[0], 'r') as fh:
        content = fh.read()

    soup = BeautifulSoup(content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        print(link)

if __name__ == "__main__":
    paths = download_urls(urls, '.')

    for path in paths:
        print('Written to', path)

    parse_html(paths)
