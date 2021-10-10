from bs4 import BeautifulSoup
import requests
import pprint


class Scrapper:

    def my_scrapper(self, coin):
        url = 'https://coinmarketcap.com/currencies/'+coin+'/'
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')

        tags = soup.find_all("td")

        pprint.pprint(tags)

    pass
