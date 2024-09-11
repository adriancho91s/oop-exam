class FileHandler:
    @staticmethod
    def read(file_path: str) -> str:
        with open(file_path, 'r') as file:
            return file.read().strip()

    @staticmethod
    def write(file_path: str, message: str):
        with open(file_path, 'w') as file:
            file.write(message)