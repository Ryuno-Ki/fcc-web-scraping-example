# FCC Web Scraping Example

This repo is accompanying an article on freeCodeCamp.
It explains how to crawl a set of static sites as well as a
Single Page Application.

## Local running

It is recommended to clone this repo into a virtual environment.
The code was written in Python 3.6 on Sabayon Linux.
However, other platforms should be supported as well.

```sh
virtualenv fcc-web-scraping-example --python=python3
cd fcc-web-scraping-example
. bin/activate
git clone https://github.com/Ryuno-Ki/fcc-web-scraping-example.git src
cd src
pip install -r requirements.txt
python scraper.py
python crawler.py
```

## Testing

For testing, you'll need to install the package locally as well.

```sh
pip install -e .
python -m pytest tests/
```

## License

GPL v3 or later. See [LICENSE](./LICENSE.txt).
