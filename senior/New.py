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
        # Sending the request
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, "html.parser")
        else:
            raise Exception("Failed to connect to the site")

    def getInfo(self):
        currency = []
        table = self.soup.find_all('tr', class_="sc-1x32wa2-4 dKDsVV")
        if not table:
            raise Exception("Failed to find the table")
        for i in table[1:6]:
            name_currency = i.find("a", class_="sc-1x32wa2-7 ciClTw")
            name = name_currency.text.strip() if name_currency else "Currency name not available"
            price = i.find_all("td")
            if len(price) >= 3:
                purchase = price[1].text.strip().replace(',', '')  # Remove commas in numbers
                sales = price[2].text.strip().replace(',', '')  # Remove commas in numbers
            else:
                purchase = "Not available"
                sales = "Not available"
            currency.append(
                {
                    "Name": name,
                    "Purchase": purchase,
                    "Sales": sales
                }
            )
        return currency

    def printInfo(self, currency):
        for i, j in enumerate(currency, start=1):
            print(i, ")")
            print("\tName:", j['Name'])
            print("\tPurchase:", j['Purchase'])
            print("\tSales:", j['Sales'])
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

    operation = int(input("1 - Buy, 2 - Sell. Please enter a number: "))
    if operation == 1:
        print("Buy")
    elif operation == 2:
        print("Sell")
    else:
        print("Invalid choice!")

    currency_choice = int(input("Select currency (number from the list): "))
    if currency_choice < 1 or currency_choice > len(currency):
        print("Invalid choice!")
        exit()

    try:
        amount = float(input("Enter the amount: "))
        selected_currency = currency[currency_choice - 1]

        if operation == 1:
            sales = float(selected_currency['Sales'])  # Convert to float
            result = amount / sales
            print(f"You can buy {result:.2f} {selected_currency['Name']}")
        else:
            purchase = float(selected_currency['Purchase'])  # Convert to float
            result = amount * purchase
            print(f"You will get {result:.2f} UAH")
    except ValueError:
        print("Invalid amount or currency data!")



