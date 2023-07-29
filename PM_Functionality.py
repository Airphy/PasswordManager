from cryptography.fernet import Fernet


class PasswordManager:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = (
            Fernet.generate_key()
        )  # This key is used for encryption and decryption
        with open(path, "wb") as file:  # wb is writing bytes mode, path is the file
            file.write(self.key)

    def load_key(self, path):
        with open(path, "rb") as file:  # rb is reading bytes
            self.key = file.read()  # reads the key which is in the file

    def create_password_file(self, path):
        self.password_file = path

    def load_password_file(self, path):
        self.password_file = path

        with open(path, "r") as file:
            for line in file:
                site, encrypted = line.split(":")
                self.password_dict[site] = (
                    Fernet(self.key).decrypt(encrypted.encode()).decode()
                )

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, "a+") as file:
                encrypted = Fernet(self.key).encrypt(password.encode())
                file.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site):
        return self.password_dict[site]


def main():
    pm = PasswordManager()
    password = {}

    print(
        """What do you want to do?
    (1) Create a new key
    (2) Load an existing key
    (3) Create a new password file
    (4) Load existing password file
    (5) Add a new password
    (6) Get a password
    (q) Quit
    """
    )

    done = False

    while not done:
        choice = input("Enter your choice: ")
        if choice == "1":
            path = input("Enter path:")
            pm.create_key(path)
        elif choice == "2":
            try:
                path = input("Enter path:")
                pm.load_key(path)
            except FileNotFoundError:
                print("File is not found, or no file to load")
        elif choice == "3":
            path = input("Enter path:")
            pm.create_password_file(path)
        elif choice == "4":
            try:
                path = input("Enter path:")
                pm.load_password_file(path)
            except FileNotFoundError:
                print("File is not found, or no file to load")
            except TypeError:
                print("No key loaded")

        elif choice == "5":
            site = input("Enter the site: ")
            password = input("Enter password: ")
            pm.add_password(site, password)
        elif choice == "6":
            try:
                site = input("What site?: ")
                print(f"Password for {site} is {pm.get_password(site)}")
            except KeyError:
                print("this site does not exist in this file")
        elif choice == "q":
            done = True
            print("Bye")
        else:
            print("Invalid")


if __name__ == "__main__":
    main()
