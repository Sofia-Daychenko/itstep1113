import requests
from bs4 import BeautifulSoup

class zolotiyvik:
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
        circlet=[]
        catalog=self.soup.find_all('div', class_="products-block-inner")
        if not catalog: raise Exception("Не вдалося знайти таблицю")
        for i in catalog:
            namecirclet=i.find("a",class_="product-item-link") #Назва монети
            name=namecirclet.text.strip() if namecirclet else "Назва каблучки відсутня"
            pricecirclet=i.find("div", class_="product-item-price-wrap") #опис фильму
            price=pricecirclet.text.strip() if pricecirclet else "Ціна каблучки відсутня"
            describecirclet=i.find("div", class_="preview-attributes")
            describe=describecirclet.text.strip() if describecirclet else "Опис каблучки відсутній"

            circlet.append(
                {
                    "Назва:":name,
                    "Ціна:":price,
                    "Опис:":describe
                }
            )
        return circlet
    def printInfo(self,laptop):
        for i,j in enumerate(laptop,start=1):
            print(i, ")")
            print("\tНазва:", j['Назва:'])
            print("\tЦіна:", j['Ціна:'])
            print("\tОпис:", j['Опис:'])
        print('='*40,'\n')

if __name__ == "__main__":
    url="https://zolotiyvik.ua/ua/kolca/"
    parse=zolotiyvik(url)
    try:
        parse.fetch_page()
        # f=parse.get_info()
        # в3.print_info()
        circlet=parse.getInfo()
        parse.printInfo(circlet)
    except Exception as e:
        print(e)