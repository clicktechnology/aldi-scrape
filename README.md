# aldi-scrape
This is a very quick scrape of Aldi's online product list using Python and Scrapy

## How to..

First, install the scrapy module.  At the command prompt, use the following command..

```
user@host ~/bin $ sudo pip install scrapy
```
Now pick a folder and pull a copy of the code to your pc
```
user@host ~/bin $ git clone https://github.com/clicktechnology/aldi-scrape.git
```
Now cd into the folder this..
```
user@host ~/bin $ cd aldi-scrape/
```

Now run the scrape..
```
user@host ~/bin/aldi-scrape $ scrapy crawl basic
```
The data is in the aldi/spiders subdirectory as output_data.csv, so cd in there.
```
user@host ~/bin/aldi-scrape $ cd aldi/spiders
```
The scraped data is in output_data.csv, ready to use.
