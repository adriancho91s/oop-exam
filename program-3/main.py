from caesar_cipher import CaesarCipher
from file_handler import FileHandler


def main():
    while True:
        print("\nCaesar Cipher CLI")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Encrypt a message from a file")
        print("4. Decrypt a message from a file")
        print("5. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            key = int(input("Enter the cipher key: "))
            message = input("Enter the message to encrypt: ")
            cipher = CaesarCipher(key)
            encrypted_message = cipher.encrypt(message)
            print(f"Encrypted message: {encrypted_message}")

        elif choice == "2":
            key = int(input("Enter the cipher key: "))
            message = input("Enter the message to decrypt: ")
            cipher = CaesarCipher(key)
            decrypted_message = cipher.decrypt(message)
            print(f"Decrypted message: {decrypted_message}")

        elif choice == "3":
            key = int(input("Enter the cipher key: "))
            file_path = input("Enter the file path: ")
            cipher = CaesarCipher(key)
            message = FileHandler.read(file_path)
            encrypted_message = cipher.encrypt(message)
            FileHandler.write(file_path, encrypted_message)
            print(f"Encrypted message written to {file_path}")

        elif choice == "4":
            key = int(input("Enter the cipher key: "))
            file_path = input("Enter the file path: ")
            cipher = CaesarCipher(key)
            message = FileHandler.read(file_path)
            decrypted_message = cipher.decrypt(message)
            FileHandler.write(file_path, decrypted_message)
            print(f"Decrypted message written to {file_path}")

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
