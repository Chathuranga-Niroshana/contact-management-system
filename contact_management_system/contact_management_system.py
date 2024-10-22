import json


def add_person():
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")

    person = {"name": name, "age": age, "email": email}
    return person


def display_people(people):
    if len(people) > 0:
        for i, person in enumerate(people):
            print(f"{i+1}. {person['name']} | {person['age']} | {person['email']}")
    else:
        print("No people in the list.")


def remove_person(people):
    for i, person in enumerate(people):
        print(f"{i+1}. {person['name']} | {person['age']} | {person['email']}")
    person_id = input("Enter index: ")
    while True:
        try:
            person_id = int(person_id)
            if person_id <= 0 or person_id > len(people):
                print("Invalid index. Please enter a valid index.")
            else:
                break
        except:
            print("Enter a number")
            break

    people.pop(person_id - 1)
    print(f"{person_id} contact deleted")


def search_person(people):
    search_name = input("Enter the name of person need to search: ").lower()
    results = []

    for person in people:
        if search_name in person["name"].lower():
            results.append(person)

    if len(results) > 0:
        display_people(results)
    else:
        print("Not available")


print("Hi, Welcome to Contact Management System.\n")

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]

while True:
    command = input("You can'Add', 'View', 'Delete', 'Search' or 'quit: ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person Added")
    elif command == "delete":
        remove_person(people)
    elif command == "search":
        search_person(people)
    elif command == "view":
        display_people(people)
    elif command == "quit":
        break
    else:
        print("Invalid command")

with open("contacts.json", "w") as f:
    json.dump({"contacts": people}, f)
