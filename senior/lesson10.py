import requests
from bs4 import BeautifulSoup

class Comfy:
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
        laptop=[]
        catalog=self.soup.find_all('div', class_="prdl-item products-catalog-grid__item prdl-item--grid")
        if not catalog: raise Exception("Не вдалося знайти таблицю")
        for i in catalog:
            nameLaptop=i.find("a",class_="prdl-item__name ellipsis-2-lines") #Назва монети
            name=nameLaptop.text.strip() if nameLaptop else "Назва ноутбука відсутня"
            priceLaptop=i.find("div", class_="products-list-item-price__actions-price-current") #опис фильму
            price = priceLaptop.text.strip() if priceLaptop else "Ціна ноутбука відсутня"

            laptop.append(
                {
                    "Назва:":name,
                    "Ціна:":price
                }
            )
        return laptop
    def printInfo(self,laptop):
        for i,j in enumerate(laptop,start=1):
            print(i,") \t", j['Назва:'],'\t', j['Ціна:'])
        print('='*40,'\n')

if __name__ == "__main__":
    url="https://comfy.ua/ua/black-friday/cat__120/?gad_source=1&gclid=Cj0KCQiAkJO8BhCGARIsAMkswyhJ-lMrSryvvEIyf_s3FPnjgF7ydctFE_R10Yj_zj9l231aRd-ZIeAaAmjrEALw_wcB"
    parse=Comfy(url)
    try:
        parse.fetch_page()
        # f=parse.get_info()
        # в3.print_info()
        laptop=parse.getInfo()
        parse.printInfo(laptop)
    except Exception as e:
        print(e)
