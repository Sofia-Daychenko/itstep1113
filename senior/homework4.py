class Product:
    def __init__(self,name="Product", price=0, availability=0):
        self.name=name
        self.price=price
        self.availablity=availability
class Cart:
    def __init__(self):
        self.items=[]

    def add(self,product, availability):
        if product.availablity < availability:
            print("{product.name} немає в наявності")
        self.items.append({"product": product, "availability": availability})
        product.update_availability(-availability)

    def remove_product(self, product_name, availability):
        """Видаляє товар з кошика."""
        for item in self.items:
            if item["product"].name == product_name:
                if item["availability"] < availability:
                    raise ValueError(f"В кошику немає такої кількості товару {product_name}.")
                item["quantity"] -= availability
                item["product"].update_quantity(availability)
                if item["quantity"] == 0:
                    self.items.remove(item)
                return
        raise ValueError(f"Товар {product_name} не знайдений в кошику.")

    def calculate_total(self):
        """Обчислює загальну вартість кошика."""
        total = sum(item["quantity"] * item["product"].price for item in self.items)
        return total
'''     
    def info(self):
        if self.passenger!=[]:
            print("Автобус(",self.model,") має пасажирів:")
            for i in self.passenger:
                print(i.name)
        else:
            print("Автобус(", self.model, ") немає пасажирів:")

p1=People('Petro',12)
p2=People('Katy',10)
b1=Bus("Marsedes")
b1.add(p1) #взаємо зв'язок між класами
b1.add(p2)
b1.info()
'''