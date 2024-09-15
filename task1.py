import json
import os


CONTACTS_FILE = 'contacts.json'


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)


def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("Contact List:")
        for index, contact in enumerate(contacts):
            print(f"{index + 1}. {contact['name']} - {contact['phone']}")


def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")


def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [c for c in contacts if search_term in c['name'] or search_term in c['phone']]
    
    if found_contacts:
        print("Search Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No contacts found.")


def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    contact = next((c for c in contacts if c['name'] == name), None)
    
    if contact:
        print(f"Updating contact: {contact['name']}")
        contact['phone'] = input(f"Enter new phone number (current: {contact['phone']}): ") or contact['phone']
        contact['email'] = input(f"Enter new email address (current: {contact['email']}): ") or contact['email']
        contact['address'] = input(f"Enter new address (current: {contact['address']}): ") or contact['address']
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    contact = next((c for c in contacts if c['name'] == name), None)
    
    if contact:
        contacts.remove(contact)
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()