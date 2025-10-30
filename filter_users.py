import json

def load_users():
    with open("users.json", "r") as f:
        return json.load(f)

def filter_users_by_name(name):
    users = load_users()
    name_lc = name.lower()
    return [u for u in users if u["name"].lower() == name_lc]

def filter_users_by_age(age):
    users = load_users()
    return [u for u in users if u["age"] == age]

def print_users(users):
    if not users:
        print("No users found.")
        return
    for u in users:
        print(u)

if __name__ == "__main__":
    option = input("Filter by 'name' or 'age'? ").strip().lower()
    if option == "name":
        q = input("Enter a name to filter users: ").strip()
        print_users(filter_users_by_name(q))
    elif option == "age":
        try:
            a = int(input("Enter an age (number): ").strip())
        except ValueError:
            print("Please enter a valid number for age.")
        else:
            print_users(filter_users_by_age(a))
    else:
        print("Filtering by that option is not yet supported.")