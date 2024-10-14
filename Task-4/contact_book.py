import csv
import os

CONTACT_FILE = 'contacts.csv'

def initialize_contact_file():
    if not os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone Number', 'Email'])

def add_contact(name, phone, email):
    with open(CONTACT_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])

def remove_contact(name):
    contacts = []
    with open(CONTACT_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != name:
                contacts.append(row)

    with open(CONTACT_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone Number', 'Email'])  # Header
        writer.writerows(contacts)

def update_contact(name, phone=None, email=None):
    contacts = []
    with open(CONTACT_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                if phone:
                    row[1] = phone
                if email:
                    row[2] = email
            contacts.append(row)

    with open(CONTACT_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone Number', 'Email'])  # Header
        writer.writerows(contacts)

def display_contacts():
    with open(CONTACT_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}')

def main():
    initialize_contact_file()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Update Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter name to remove: ")
            remove_contact(name)
        elif choice == '3':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            update_contact(name, phone if phone else None, email if email else None)
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
