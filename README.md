# Worldometers COVID-19 (Corona) data scraper

This is a scrapy scraper to crawl data from
[worldometers.info/coronavirus](https://www.worldometers.info/coronavirus/)

  - Easily download latest COVID-19 data
  - Download data as csv or json to perform analysis
  - Or use in web application to populate data online



### Installation
Clone the repo on your system.
Install the dependencies and crawl data using following commands.

```sh
$ pip install -r requirements.txt
$ scrapy crawl worldometers -o data.json
$ scrapy crawl worldometers -o data.csv
```

You can eiter use -o data.json or data.csv to download data as json or csv.