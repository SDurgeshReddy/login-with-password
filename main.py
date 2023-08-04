def create_account():
    print("Creating a new account.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

def login():
    print("Login to your account.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

def main():
    accounts = {}

    while True:
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            username, password = create_account()
            accounts[username] = password
            print("Account created successfully!")

        elif choice == 2:
            username, password = login()
            if username in accounts and accounts[username] == password:
                print("Login successful!")
            else:
                print("Invalid username or password. Please try again.")

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
