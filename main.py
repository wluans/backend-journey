users = []

def create_user(name, email):
    user = {
        "name": name,
        "email": email
    }
    users.append(user)
    print("User created successfully.")


def list_users():
    if not users:
        print("No users registered.")
        return

    for index, user in enumerate(users, start=1):
        print(f"{index} - {user['name']} | {user['email']}")


def menu():
    while True:
        print("\n=== USER SYSTEM ===")
        print("1 - Create user")
        print("2 - List users")
        print("3 - Exit")

        option = input("Choose an option: ")

        if option == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            create_user(name, email)

        elif option == "2":
            list_users()

        elif option == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()
