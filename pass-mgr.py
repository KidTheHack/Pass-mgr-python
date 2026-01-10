from cryptography.fernet import Fernet, InvalidToken

def cls():
    print("\x1b[H\x1b[2J\x1b[3J")

""" Show which key and password file are currently loaded. """
def info_job(name_key, pass_file):
    if name_key:
        print(f"\nKey: {name_key}")

    else:
        print("\nKey not loaded")

    if pass_file:
        print(f"Password file: {pass_file}\n")

    else:
        print("Password file not loaded\n")

# ========== Key functions =========#

""" Generate and save a new Fernet key at the given path. """
def create_key(path):
    with open(path, 'wb') as f:
        key = Fernet.generate_key()
        f.write(key)

""" Load an existing Fernet key from file. """
def load_key(path):
    try:
        with open(path, 'rb') as f:
            key = f.read()

        return key

    except FileNotFoundError:
        print("Key not found!")

# =========== Password file functions ==============#

""" Load an existing Fernet key from file. """
def update_pass_file(path, pass_dict, mode):
    with open(path, mode) as f:
        for key, value in pass_dict.items():
            f.write("[" + key + "]\n")
            for Ikey, Ivalue in value.items():
                f.write(Ikey + ":" + Ivalue + "\n")

""" Encrypt the service, username and password and create a new file. """
def create_new_pass_file(path, key, pass_dict, service, username, password):
    fernet = Fernet(key)

    service = fernet.encrypt(service.encode()).decode()
    username = fernet.encrypt(username.encode()).decode()
    password = fernet.encrypt(password.encode()).decode()

    pass_dict.update({service: {username: password}})

    update_pass_file(path, pass_dict, 'w')

""" Load an existing password file and store encrypted entries into pass_dict. """
def load_pass_file(path, pass_dict):
    try:
        with open(path, 'r') as f:
            for r in f:
                r = r.strip()

                if not r:
                    continue

                if r.startswith('[') and r.endswith(']'):
                    current_key = r[1:-1]
                    pass_dict[current_key] = {}

                elif ':' in r and current_key:
                    key, value = r.split(':', 1)
                    pass_dict[current_key][key] = value

            return pass_dict

    except FileNotFoundError:
        print("Invalid password file!")
        return

# ============= Service functions =============#

""" Add a new encrypted service/username/password to the password file. """
def add_service(path, key, pass_dict, service, username, password):
    fernet = Fernet(key)

    service = fernet.encrypt(service.encode()).decode()
    username = fernet.encrypt(username.encode()).decode()
    password = fernet.encrypt(password.encode()).decode()

    pass_dict[service] = {username: password}

    update_pass_file(path, pass_dict, 'w')

""" Decrypt and print login credentials for a given service. """
def get_service(name_service, pass_dict, key):
    fernet = Fernet(key)

    for service, usr_and_pass in pass_dict.items():
        try:
            service = fernet.decrypt(service.encode()).decode()

        except InvalidToken:
            print("Incorrect key for this password file!")
            return


        if service == name_service:
            for username, password in usr_and_pass.items():
                username = fernet.decrypt(username.encode()).decode()
                password = fernet.decrypt(password.encode()).decode()

                print(f"Service: {service}\nUsername: {username} | Password: {password}")

""" Delete the specified service. """
def delete_service(name_service, pass_dict, key, path):
    fernet = Fernet(key)

    search = False
    for i in pass_dict:
       try:
            service = fernet.decrypt(i.encode()).decode()
       except InvalidToken:
            print("Incorrect key for this password file!")
            return

       if service == name_service:
            search = True
            break

    if search:
        del pass_dict[i]
        print(f"Service {name_service} delited!")
        update_pass_file(path, pass_dict, 'w')

    else:
        print("Service not fount!")

""" List all decrypted service names stored in the password file. """
def list_service(pass_dict, key):
    fernet = Fernet(key)
    print("Service:")
    for i in pass_dict:
        try:
            service = fernet.decrypt(i.encode()).decode()
            print(service)

        except InvalidToken:
            print("Invalid key for this password file!")
            return

# ========== Main function ==========#

def main():
    cls()

    key = None
    name_key = None
    pass_file = None
    pass_dict = {}

    while True:
        info_job(name_key, pass_file)

        print("""
              Menu:
              1. Create a new key.
              2. Load an existing key.
              3. Create a new password file.
              4. Load an existing password file.
              5. Add a new service.
              6. List all services in the current password file.
              7. Get a service (username and password).
              8. Delete a service.
              (q) Quit.\n""")

        choice = input("Enter yuor choice: ")
        cls()

        if choice == "1":
            name_key = input("Enter a name for the new key: ")
            create_key(name_key)

            key = load_key(name_key)
            print("Key generated and loaded.")

        elif choice == "2":
            name_key = input("Enter a name of an existing key: ")
            key = load_key(name_key)
            print("Key loaded successfully.")

        elif choice == "3":
            if key:
                pass_file = input("Enter a name for the new password file: ")
                service = input("Enter the service name: ")
                username = input("Enter the username: ")
                password = input("Enter the password: ")

                create_new_pass_file(pass_file, key, pass_dict, service, username, password)

                pass_dict.clear()

                load_pass_file(pass_file, pass_dict)
                print("Password file generated successfully.")

            else:
                print("Please generate or load key first!")

        elif choice == "4":
            if key:
                pass_file = input("Enter the name of an existing password file: ")

                pass_dict.clear()
                load_pass_file(pass_file, pass_dict)

                print("Password file loaded successfully.")

            else:
                print("Please generate or load a valid key first!")

        elif choice == "5":
            if key and pass_file:
                service = input("Enter the service name: ")
                username = input("Enter the username: ")
                password = input("Enter the password: ")

                add_service(pass_file, key, pass_dict, service, username, password)

                load_pass_file(pass_file, pass_dict)

                print("Service added!")

            else:
                print("Please generate or load a valid key and password file!")

        elif choice == "6":
            if key and pass_dict:
                list_service(pass_dict, key)

            else:
                print("Please generate or load a valid key and password file!")
                
        elif choice == "7":
            if key and pass_dict:
                list_service(pass_dict, key)
            
                name_service = input("Enter the name of the service you want to retrive: ")

                get_service(name_service, pass_dict, key)

            else:
                print("Please generate or load a valid key and password file!")

        elif choice == "8":
            if key and pass_dict:
                list_service(pass_dict, key)

                name_service = input("Enter the name of the service you want to delete: ")

                delete_service(name_service, pass_dict, key, pass_file)

            else:
                print("Please generate or load a valid key and password file!")

        elif choice.lower() == "q":
            print("Bye bye!")
            break

        else:
            print("Invalid choice!")

# ====== Entry point =========#

if __name__ == "__main__":
    main()


