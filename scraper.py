from os import path
from pathlib import PurePath
import sys
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
  'https://www.gesetze-im-internet.de/gg/art_16a.html',
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
            else:
                print('Bad response for', url, response.status_code)
        except requests.exceptions.ConnectionError as exc:
            print(exc)
    
        with open(file_path, 'w') as fh:
            fh.write(text)

        paths.append(file_path)

    return paths

def parse_html(path):
    with open(path, 'r') as fh:
        content = fh.read()

    return BeautifulSoup(content, 'html.parser')

def download():
    return download_urls(urls, '.')

def extract(path):
    return parse_html(path)

def transform(soup):
    container = soup.find(id='container')
    if container is not None:
        return container.get_text()

def load(key, value):
    d = {}
    d[key] = value
    return d

def run_single(path):
    soup = extract(path)
    content = transform(soup)
    unserialised = load(path, content.strip() if content is not None else '')
    return unserialised

def run_everything():
    l = []

    paths = download()
    for path in paths:
        print('Written to', path)
        l.append(run_single(path))

    print(l)

if __name__ == "__main__":
    args = sys.argv

    if len(args) is 1:
      run_everything()
    else:
        if args[1] == 'download':
            download()
            print('Done')
        if args[1] == 'parse':
            path = args[2]
            result = run_single(path)
            print(result)
