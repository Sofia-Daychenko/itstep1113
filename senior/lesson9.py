import requests
from bs4 import BeautifulSoup

class Coinmarket:
    def __init__(self,url):
        self.url=url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup=None

    def fetch_page(self):
            #Відправка запроса
            response = requests.get(self.url, headers=self.headers)
            if response.status_code==200:
                self.soup=BeautifulSoup(response.text,"html.parser")
            else:
                raise Exception("Не вдалося під'єднатися до сайту")
    def getInfo(self):
        coins=[]
        table=self.soup.find('tbody')
        if not table: raise Exception("Не вдалося знайти таблицю")
        rows=table.find_all('tr')[:5]
        for i in rows:
            nameCoin=i.find("p",class_="coin-item-name") #Назва монети
            name=nameCoin.text.strip() if nameCoin else "Назва монети відсутня"
            priceCoin=i.find("span") #опис фильму
            price = priceCoin.text.strip() if priceCoin else "Ціна монети відсутня"

            coins.append(
                {
                    "Назва:":name,
                    "Ціна:":price
                }
            )
        return coins
    def printInfo(self,coins):
        for i,j in enumerate(coins,start=1):
            print(i,") Монета")
            print('\t','Назва:',coins['Назва:'])
            print('\t', 'Ціна:', coins['Ціна:'])
        print('='*40,'\n')

if __name__ == "__main__":
    url="https://coinmarketcap.com/"
    parse=Coinmarket(url)
    try:
        parse.fetch_page()
        # f=parse.get_info()
        # в3                                                                                            .print_info()
        coin=в3                                                                                             .getInfo()
    except Exception as e:
        print(e)

