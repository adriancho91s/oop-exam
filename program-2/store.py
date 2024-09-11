from product import Product
from client import Client

class Store:
    def __init__(self):
        self.products = []
        self.clients = []

    def add_product(self, product: Product):
        self.products.append(product)

    def add_client(self, client: Client):
        self.clients.append(client)

    def sell_product(self, client_id: int, product_id: int, quantity: int):
        client = next((client for client in self.clients if client.id == client_id), None)
        product = next((product for product in self.products if product.id == product_id), None)
        if client and product:
            return client.buy(product, quantity)
        return False

    def show_products(self):
        if not self.products:
            print("No products available")
            return
        for product in self.products:
            product.show_info()

    def show_clients(self):
        if not self.clients:
            print("No clients registered")
            return
        for client in self.clients:
            client.show_info()

    def save_data(self, file: str):
        with open(file, "w") as f:
            f.write("Products\n")
            for product in self.products:
                f.write(f"{product.name},{product.id},{product.price},{product.stock}\n")
            f.write("Clients\n")
            for client in self.clients:
                f.write(f"{client.name},{client.id},{client.balance}\n")

    def load_data(self, file: str):
        try:
            with open(file, "r") as f:
                self.products = []
                self.clients = []
                line = f.readline().strip()
                while line:
                    if line == "Products":
                        line = f.readline().strip()
                        while line != "Clients" and line:
                            name, id, price, stock = line.split(",")
                            self.products.append(Product(name, int(id), float(price), int(stock)))
                            line = f.readline().strip()
                    if line == "Clients":
                        line = f.readline().strip()
                        while line:
                            name, id, balance = line.split(",")
                            self.clients.append(Client(name, int(id), float(balance)))
                            line = f.readline().strip()
                    line = f.readline().strip()
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False