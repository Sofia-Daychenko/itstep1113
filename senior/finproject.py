import requests
from bs4 import BeautifulSoup


class Minfin:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup = None

    def fetch_page(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, "html.parser")
        else:
            raise Exception("Не вдалося під'єднатися до сайту")

    def getInfo(self):
        currency = []
        table = self.soup.find_all('tr', class_="sc-1x32wa2-4 dKDsVV")
        if not table:
            raise Exception("Не вдалося знайти таблицю")
        for i in table[1:6]:
            name_currency = i.find("a", class_="sc-1x32wa2-7 ciClTw")
            name = name_currency.text.strip() if name_currency else "Назва відсутня"
            price = i.find_all("td")
            if len(price) >= 3:
                purchase = price[1].text.strip().replace(',', '')
                sales = price[2].text.strip().replace(',', '')
            else:
                purchase = "Не доступний"
                sales = "Не доступний"
            currency.append(
                {
                    "Назва": name,
                    "Купити": purchase,
                    "Продати": sales
                }
            )
        return currency

    def printInfo(self, currency):
        for i, j in enumerate(currency, start=1):
            print(i, ")")
            print("\tНазва", j['Назва'])
            print("\tКупити:", j['Купити'])
            print("\tПродати:", j['Продати'])
        print('=' * 40, '\n')


if __name__ == "__main__":
    url = "https://minfin.com.ua/ua/currency/"
    parse = Minfin(url)
    try:
        parse.fetch_page()
        currency = parse.getInfo()
        parse.printInfo(currency)
    except Exception as e:
        print(e)

    operation = int(input("1 - Купити, 2 - Продати. Введіть цифру: "))
    if operation == 1:
        print("Купити")
    elif operation == 2:
        print("Продати")
    else:
        print("Некоректний вибір!")

    currency_choice = int(input("Введіть цифру купюри: "))
    if currency_choice < 1 or currency_choice > len(currency):
        print("Некоректний вибір!")
        exit()

    try:
        amount = float(input("Введіть суму: "))
        selected_currency = currency[currency_choice - 1]

        if operation == 2:
            sales = float(selected_currency['Продати'])
            result = amount / sales
            print(f"Ви можете продати {result:.2f} {selected_currency['Назва']}")
        elif operation == 1:
            purchase = float(selected_currency['Купити'])
            result = amount * purchase
            print(f"Ви маєте {result:.2f} UAH")
    except ValueError:
        print("Некоректний вибір")


