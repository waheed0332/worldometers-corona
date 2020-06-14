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

### Data Description

Downloaded data will have following columns.

| Column | Description |
| ------ | ------ |
| Country, Others |
| State |
| Continent |
| Total Cases |
| New Cases |
| Total Deaths |
| New Deaths |
| Total Recovered |
| New Recovered |
| Active Cases |
| Serious, Critical |
| Total Cases / 1M Polulation |
| Deaths / 1M Population |
| Total Tests |
| Tests / 1M Population |
| Population |
| 1 Case ever X People |
| 1 Death ever X People |
| 1 Test ever X People |