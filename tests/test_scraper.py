from unittest import TestCase

from bs4 import BeautifulSoup

from fcc.scraper import extract, load, transform

class ScraperTest(TestCase):
    def test_extract(self):
        filepath = 'stub.html'
        actual = extract(filepath)
        assert isinstance(actual, BeautifulSoup)

    def test_transform(self):
        fakeHtml = '<html><body><div id="container">Test</div></body></html>'
        soup = BeautifulSoup(fakeHtml, 'html.parser')
        actual = transform(soup)
        assert actual == 'Test'

    def test_load(self):
        assert True
