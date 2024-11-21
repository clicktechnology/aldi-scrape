# Aldi-scrape

This is a very quick scrape of Aldi's online product list using Python and Scrapy

## How to

First, clone the repo and install the requirements.

```bash
cd aldi-scrape
python -m pip install -r requirements.txt
source venv/bin/activate
```

Now run the scrape..

```bash
scrapy crawl basic
```

The data is in the aldi/spiders subdirectory as output_data.csv, so cd in there.

```bash
cd aldi/spiders
```

The scraped data is in output_data.csv, ready to use.
