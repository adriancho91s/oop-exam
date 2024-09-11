class Product:
    def __init__(self, name: str, id: int, price: float, stock: int):
        self.name = name
        self.id = id
        self.price = price
        self.stock = stock

    def decrease_stock(self, quantity: int):
        self.stock -= quantity

    def increase_stock(self, quantity: int):
        self.stock += quantity

    def show_info(self):
        print(f"Name: {self.name}\nID: {self.id}\nPrice: {self.price}\nStock: {self.stock}\n")
