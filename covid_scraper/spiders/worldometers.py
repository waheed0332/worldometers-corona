# -*- coding: utf-8 -*-
import scrapy


class WorldometersSpider(scrapy.Spider):

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
    }

    name = 'worldometers'
    allowed_domains = ['worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        records = response.xpath('//table[@id="main_table_countries_today"]/tbody[not(@id) and not(@class)]/tr[not(contains(@class, "total_row_world"))]')

        for record in records:
            country = record.xpath('./td[position()=2]//text()').extract_first()
            state = ''
            continent = record.xpath('./td[position()=16]//text()').extract_first()
            total_cases = record.xpath('./td[position()=3]//text()').extract_first()
            new_cases = record.xpath('./td[position()=4]//text()').extract_first()
            total_deaths = record.xpath('./td[position()=5]//text()').extract_first()
            new_deaths = record.xpath('./td[position()=6]//text()').extract_first()
            total_recovered = record.xpath('./td[position()=7]//text()').extract_first()
            new_recovered = record.xpath('./td[position()=8]//text()').extract_first()
            active_cases = record.xpath('./td[position()=9]//text()').extract_first()
            serious_critical = record.xpath('./td[position()=10]//text()').extract_first()
            total_cases_per_million = record.xpath('./td[position()=11]//text()').extract_first()
            deaths_per_million = record.xpath('./td[position()=12]//text()').extract_first()
            total_tests = record.xpath('./td[position()=13]//text()').extract_first()
            total_tests_per_million = record.xpath('./td[position()=14]//text()').extract_first()
            population = record.xpath('./td[position()=15]//text()').extract_first()
            one_case_per_x_people = record.xpath('./td[position()=17]//text()').extract_first()
            one_death_per_x_people = record.xpath('./td[position()=18]//text()').extract_first()
            one_test_per_x_people = record.xpath('./td[position()=19]//text()').extract_first()
            country_url = record.xpath('./td[position()=2]/a/@href').extract_first()


            if country_url != None:
                yield scrapy.Request(response.urljoin(country_url), callback=self.parse_country, meta={
                    'Country, Others': country,
                    'State': state,
                    'Continent': continent,
                    'Total Cases': total_cases,
                    'New Cases': new_cases,
                    'Total Deaths': total_deaths,
                    'New Deaths': new_deaths,
                    'Total Recovered': total_recovered,
                    'New Recovered': new_recovered,
                    'Active Cases': active_cases,
                    'Serious, Critical': serious_critical,
                    'Total Cases / 1M Polulation': total_cases_per_million,
                    'Deaths / 1M Population': deaths_per_million,
                    'Total Tests': total_tests,
                    'Tests / 1M Population': total_tests_per_million,
                    'Population': population,
                    '1 Case ever X People': one_case_per_x_people,
                    '1 Death ever X People': one_death_per_x_people,
                    '1 Test ever X People': one_test_per_x_people
                })

            else:
                 yield {
                    'Country, Others': country,
                    'State': '',
                    'Continent': continent,
                    'Total Cases': total_cases,
                    'New Cases': new_cases,
                    'Total Deaths': total_deaths,
                    'New Deaths': new_deaths,
                    'Total Recovered': total_recovered,
                    'New Recovered': new_recovered,
                    'Active Cases': active_cases,
                    'Serious, Critical': serious_critical,
                    'Total Cases / 1M Polulation': total_cases_per_million,
                    'Deaths / 1M Population': deaths_per_million,
                    'Total Tests': total_tests,
                    'Tests / 1M Population': total_tests_per_million,
                    'Population': population,
                    '1 Case ever X People': one_case_per_x_people,
                    '1 Death ever X People': one_death_per_x_people,
                    '1 Test ever X People': one_test_per_x_people
                }

    def parse_country(self, response):
        result = response.xpath('//table')

        if len(result)==0:
            del response.meta['download_latency']
            del response.meta['download_slot']
            del response.meta['download_timeout']
            del response.meta['depth']
            yield response.meta

        else:
            records = response.xpath('//table[contains(@id, "table_countries_today")]/tbody[position()=1]/tr[position()>1]')
            for record in records:
                yield {
                    'Country, Others': response.meta['Country, Others'],
                    'State': (''.join(record.xpath('./td[position()=1]//text()').extract())).strip(),
                    'Continent': response.meta['Country, Others'],
                    'Total Cases': (''.join(record.xpath('./td[position()=2]//text()').extract())).strip(),
                    'New Cases': (''.join(record.xpath('./td[position()=3]//text()').extract())).strip(),
                    'Total Deaths': (''.join(record.xpath('./td[position()=4]//text()').extract())).strip(),
                    'New Deaths': (''.join(record.xpath('./td[position()=5]//text()').extract())).strip(),
                    'Total Recovered': '',
                    'New Recovered': '',
                    'Active Cases': (''.join(record.xpath('./td[position()=6]//text()').extract())).strip(),
                    'Serious, Critical': '',
                    'Total Cases / 1M Polulation': (''.join(record.xpath('./td[position()=7]//text()').extract())).strip(),
                    'Deaths / 1M Population': (''.join(record.xpath('./td[position()=8]//text()').extract())).strip(),
                    'Total Tests': (''.join(record.xpath('./td[position()=9]//text()').extract())).strip(),
                    'Tests / 1M Population': (''.join(record.xpath('./td[position()=10]//text()').extract())).strip(),
                    'Population': '',
                    '1 Case ever X People': '',
                    '1 Death ever X People': '',
                    '1 Test ever X People': ''
                }