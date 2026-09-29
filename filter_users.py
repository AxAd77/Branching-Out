import json


def load_users():
    with open("users.json", "r") as file:
        return json.load(file)


def print_results(users):
    if not users:
        print("Keine Benutzer gefunden.")
        return
    for user in users:
        print(user)


def filter_users_by_name(name):
    users = load_users()
    filtered_users = [
        user for user in users
        if user.get("name", "").lower() == name.lower()
    ]
    print_results(filtered_users)


def filter_users_by_email(email):
    users = load_users()
    filtered_users = [
        user for user in users
        if user.get("email", "").lower() == email.lower()
    ]
    print_results(filtered_users)


def filter_users_by_age(age):
    users = load_users()
    filtered_users = [user for user in users if user.get("age") == age]
    print_results(filtered_users)


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? (name, email, age): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    elif filter_option == "age":
        age_input = input("Enter an age to filter users: ").strip()
        try:
            filter_users_by_age(int(age_input))
        except ValueError:
            print(f"'{age_input}' is not a valid age. Please enter a whole number.")
    else:
        print(
            f"'{filter_option}' is not a supported option. "
            "Please choose one of: name, email, age."
        )
