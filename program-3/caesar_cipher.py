

class CaesarCipher:
    def __init__(self, key: int):
        self.key = key
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.alphabet_upper = self.alphabet.upper()

    def encrypt(self, message: str) -> str:
        encrypted_message = []
        for char in message:
            if char in self.alphabet:
                index = (self.alphabet.index(char) - self.key) % 26
                encrypted_message.append(self.alphabet[index])
            elif char in self.alphabet_upper:
                index = (self.alphabet_upper.index(char) - self.key) % 26
                encrypted_message.append(self.alphabet_upper[index])
            else:
                encrypted_message.append(char)
        return ''.join(encrypted_message)

    def decrypt(self, message: str) -> str:
        decrypted_message = []
        for char in message:
            if char in self.alphabet:
                index = (self.alphabet.index(char) + self.key) % 26
                decrypted_message.append(self.alphabet[index])
            elif char in self.alphabet_upper:
                index = (self.alphabet_upper.index(char) + self.key) % 26
                decrypted_message.append(self.alphabet_upper[index])
            else:
                decrypted_message.append(char)
        return ''.join(decrypted_message)
