"""
This code will download a set of static files and parse them for a WordCloud.
Copyright (C) 2020 - André Jaenisch

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.`
"""
from os import path
from pathlib import Path, PurePath
import sys

from bs4 import BeautifulSoup
import requests
from wordcloud import WordCloud

STOPWORDS_ADDENDUM = [
    'Das',
    'Der',
    'Die',
    'Diese',
    'Eine',
    'In',
    'InhaltsverzeichnisGrundgesetz',
    'im',
    'Jede',
    'Jeder',
    'Kein',
    'Sie',
    'Soweit',
    'Über'
]
STOPWORDS_FILE_PATH = 'stopwords.txt'
STOPWORDS_URL = 'https://raw.githubusercontent.com/stopwords-iso/stopwords-de/master/stopwords-de.txt'


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

def download_stopwords():
    stopwords = ''

    try:
        response = requests.get(STOPWORDS_URL)
        if response.ok:
            stopwords = response.text
        else:
            print('Bad response for', url, response.status_code)
    except requests.exceptions.ConnectionError as exc:
        print(exc)

    with open(STOPWORDS_FILE_PATH, 'w') as fh:
        fh.write(stopwords)

    return stopwords

def download(urls):
    return download_urls(urls, '.')

def extract(path):
    return parse_html(path)

def transform(soup):
    container = soup.find(id='container')
    if container is not None:
        return container.get_text()

def load(filename, text):
    if Path(STOPWORDS_FILE_PATH).exists():
        with open(STOPWORDS_FILE_PATH, 'r') as fh:
            stopwords = fh.readlines()
    else:
        stopwords = download_stopwords()

    # Strip whitespace around
    stopwords = [stopword.strip() for stopword in stopwords]
    # Extend stopwords with own ones, which were determined after first run
    stopwords = stopwords + STOPWORDS_ADDENDUM

    try:
        cloud = WordCloud(stopwords=stopwords).generate(text)
        cloud.to_file(filename.replace('.html', '.png'))
    except ValueError:
        print('Could not generate word cloud for', key)

def run_single(path):
    soup = extract(path)
    content = transform(soup)
    load(path, content.strip() if content is not None else '')

def run_everything():
    with open('urls.txt', 'r') as fh:
        urls = fh.readlines()
    urls = [url.strip() for url in urls]

    paths = download(urls)
    for path in paths:
        print('Written to', path)
        run_single(path)
    print('Done')

if __name__ == "__main__":
    args = sys.argv

    if len(args) is 1:
      run_everything()
    else:
        if args[1] == 'download':
            download([args[2]])
            print('Done')
        if args[1] == 'parse':
            path = args[2]
            run_single(path)
            print('Done')
