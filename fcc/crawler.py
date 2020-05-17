"""
This code will use Firefox to open a SPA site, extract some data and render a
WordCloud.
Copyright (C) 2020 - André Jaenisch

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.`
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wordcloud import WordCloud

def extract(url):
    elem = None
    driver = webdriver.Firefox()
    driver.get(url)

    try:
        found = WebDriverWait(driver, 10).until(
            EC.visibility_of(
                driver.find_element(By.TAG_NAME, "article")
            )
        )
        # Make a copy of relevant data, because Selenium will throw if
        # you try to access the properties after the driver quit
        elem = {
          "text": found.text
        }
    finally:
        driver.close()

    return elem

def transform(elem):
    return elem["text"]

def load(text, filepath):
    cloud = WordCloud().generate(text)
    cloud.to_file(filepath)

if __name__ == "__main__":
    url = "https://angular.io/"
    filepath = "angular.png"

    elem = extract(url)
    if elem is not None:
        text = transform(elem)
        load(text, filepath)
    else:
        print("Sorry, could not extract data")
