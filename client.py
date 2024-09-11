from product import Product

class Client:
    def __init__(self, name: str, id: int, balance: float):
        self.name = name
        self.id = id
        self.balance = balance

    def buy(self, product: Product, quantity: int):
        if product.stock >= quantity and self.balance >= product.price * quantity:
            product.decrease_stock(quantity)
            self.balance -= product.price * quantity
            return True
        return False

    def show_info(self):
        print(f"Name: {self.name}\nID: {self.id}\nBalance: {self.balance}\n")