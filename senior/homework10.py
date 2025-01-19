import requests
from bs4 import BeautifulSoup

class bookclub:
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
        book=[]
        catalog=self.soup.find_all('div', class_="top_id_blocks")
        if not catalog: raise Exception("Не вдалося знайти таблицю")
        for i in catalog:
            namebook=i.find("div",class_="prname")
            name=namebook.text.strip() if namebook else "Назва книги відсутня"
            authorbook = i.find("div", class_="prauthor")
            author = authorbook.text.strip() if authorbook else "Автор книги відсутній"
            pricebook=i.find("td", class_="priceAct")
            price=pricebook.text.strip() if pricebook else "Ціна книги відсутня"

            book.append(
                {
                    "Назва:":name,
                    "Ціна:":price,
                    "Автор:":author
                }
            )
        return book
    def printInfo(self,book):
        for i,j in enumerate(book,start=1):
            print(i, ")")
            print("\tНазва:", j['Назва:'])
            print("\tАвтор:", j['Автор:'])
            print("\tЦіна:", j['Ціна:'])
        print('='*40,'\n')

if __name__ == "__main__":
    url="https://bookclub.ua/?gad_source=1&gclid=Cj0KCQiAv628BhC2ARIsAIJIiK_nJ-8thywuVLefhxCGryvPSB1D25LwMUljdYxVeZ04xI0ql137_EcaArHyEALw_wcB"
    parse=bookclub(url)
    try:
        parse.fetch_page()
        # f=parse.get_info()
        # в3.print_info()
        book=parse.getInfo()
        parse.printInfo(book)
    except Exception as e:
        print(e)