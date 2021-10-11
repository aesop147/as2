import requests
from bs4 import BeautifulSoup

class scrappingcoinmarket:
    def __init__(self):
        self.arr = []

    def result(self, cryptoname):
        r = requests.get('https://coinmarketcap.com/all/views/all/')
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('tbody')
        for row in table.find_all('tr'):
            try:
                if cryptoname == row.find('a', class_='cmc-table__column-name--name cmc-link').text:
                    s = row.find('td',
                                      class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--hide-sm cmc-table__cell--sort-by__symbol').text
                    mkt = row.find('td',
                                       class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap').find(
                        'span', class_='sc-1ow4cwt-1 ieFnWP').text
                    price = row.find('td',
                                     class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price').text
                    circ = row.find('td',
                                       class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply").text
                    vol = row.find('td',
                                      class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__volume-24-h").text
                    h1 = row.find('td',
                                    class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-1-h').text
                    h24 = row.find('td',
                                     class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-24-h').text
                    d7 = row.find('td',
                                    class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-7-d').text
                    self.arr = [row.find('a', class_='cmc-table__column-name--name cmc-link').text, s, mkt, price, circ, vol, h1, h24, d7]
                    break
                else:
                    continue
            except AttributeError:
                continue
        for i in self.arr:
            print(i)
