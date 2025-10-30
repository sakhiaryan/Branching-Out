import json


def load_users():
    with open("users.json", "r") as f:
        return json.load(f)


def filter_users_by_name(name):
    users = load_users()
    return [u for u in users if u["name"].lower() == name.lower()]


def filter_users_by_age(age):
    users = load_users()
    return [u for u in users if u["age"] == age]


def filter_users_by_email(email):
    users = load_users()
    email_lc = email.lower()
    # erlaubt Teil-Übereinstimmungen (z. B. "gmail" findet alle gmail-Adressen)
    return [u for u in users if email_lc in u["email"].lower()]


def print_users(users):
    if not users:
        print("No users found.")
        return
    for u in users:
        print(u)


if __name__ == "__main__":
    option = input("Filter by 'name', 'age', or 'email'? ").strip().lower()

    if option == "name":
        query = input("Enter a name to filter users: ").strip()
        print_users(filter_users_by_name(query))

    elif option == "age":
        try:
            query = int(input("Enter an age (number): ").strip())
            print_users(filter_users_by_age(query))
        except ValueError:
            print("❗ Please enter a valid number for age.")

    elif option == "email":
        query = input("Enter part or full email to filter: ").strip()
        print_users(filter_users_by_email(query))

    else:
        print("Filtering by that option is not yet supported.")