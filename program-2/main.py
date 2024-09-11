from product import Product
from client import Client
from store import Store

if __name__ == "__main__":
    store = Store()

    load = input("Do you want to load data from the file? (yes/no): ").strip().lower()
    file_path = "store.dat"
    if load == "yes":
        file_path = input("Enter the file path to load/save data (default: store.dat): ").strip()
        if not file_path:
            file_path = "store.dat"
        if store.load_data(file_path):
            print("Data loaded successfully.")
    elif load == "no":
        print("Starting with an empty store.")
    else:
        print("Invalid option. Exiting.")
        exit()

    while True:
        print("\nSelect your role:")
        print("1. Client")
        print("2. Admin")
        print("3. Exit")
        role = input("Select an option: ").strip()

        if role == "1":
            try:
                client_id = int(input("Enter your client ID: "))
            except ValueError:
                print("Invalid ID. Please try again.")
                continue
            client = next((client for client in store.clients if client.id == client_id), None)
            if not client:
                print("Client not found. Creating a new client.")
                name = input("Enter your name: ")
                balance = float(input("Enter your balance: "))
                client = Client(name, client_id, balance)
                store.add_client(client)
            while True:
                print("\nClient Menu:")
                print("1. View available products")
                print("2. View personal information")
                print("3. Buy a product")
                print("4. Save data to file")
                print("5. Log out")
                client_option = input("Select an option: ").strip()

                if client_option == "1":
                    store.show_products()

                elif client_option == "2":
                    client.show_info()

                elif client_option == "3":
                    store.show_products()
                    try:
                        product_id = int(input("Enter the product ID you want to buy: "))
                    except ValueError:
                        print("Invalid ID. Please try again.")
                        continue
                    product = next((product for product in store.products if product.id == product_id), None)
                    if not product:
                        print("Product not found")
                        continue
                    quantity = int(input("Enter the quantity you want to buy: "))
                    if store.sell_product(client_id, product_id, quantity):
                        print("Purchase successful")
                    else:
                        print("Purchase failed")

                elif client_option == "4":
                    store.save_data(file_path)
                    print("Data saved successfully.")

                elif client_option == "5":
                    print("Logging out.")
                    break

                else:
                    print("Invalid option. Please try again.")

        elif role == "2":
            while True:
                print("\nAdmin Menu:")
                print("1. Add a new product")
                print("2. Show all products")
                print("3. Show all clients")
                print("4. Add a new client")
                print("5. Save data to file")
                print("6. Exit to main menu")
                admin_option = input("Select an option: ").strip()

                if admin_option == "1":
                    name = input("Enter the product name: ")
                    try:
                        id = int(input("Enter the product ID: "))
                    except ValueError:
                        print("Invalid ID. Please try again.")
                        continue
                    try:
                        price = float(input("Enter the product price: "))
                        stock = int(input("Enter the product stock: "))
                    except ValueError:
                        print("Invalid input. Please try again.")
                        continue
                    product = Product(name, id, price, stock)
                    store.add_product(product)
                    product.show_info()

                elif admin_option == "2":
                    store.show_products()

                elif admin_option == "3":
                    store.show_clients()

                elif admin_option == "4":
                    name = input("Enter the client name: ")
                    id = int(input("Enter the client ID: "))
                    balance = float(input("Enter the client balance: "))
                    client = Client(name, id, balance)
                    store.add_client(client)
                    client.show_info()

                elif admin_option == "5":
                    store.save_data(file_path)
                    print("Data saved successfully.")

                elif admin_option == "6":
                    break

                else:
                    print("Invalid option. Please try again.")

        elif role == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")