from setuptools import setup

setup(
    version="0.1.0",
    name="fcc",
    author="André Jaenisch",
    author_email="andre.jaenisch@posteo.de",
    description="FCC Web Scraping Example",
    packages=["fcc", ],
    install_requires=["beautifulsoup4", "requests", "wordcloud", "selenium"],
    url="https://github.com/Ryuno-Ki/fcc-web-scraping-example",
    license="GPL-3.0-or-later",
    data_files=[("", ["LICENSE.txt", ])],
    platforms=["Linux", ],
    include_package_data=True,
    project_urls={
      "Code": "https://github.com/Ryuno-Ki/fcc-web-scraping-example",
      "Issue tracker": "https://github.com/Ryuno-Ki/fcc-web-scraping-example/issues"
    }
)
