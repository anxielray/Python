class PhoneBook:
    """A simple phone book application for storing and managing contacts."""
    
    def __init__(self):
        """Initialize an empty phone book."""
        self.contacts = {}  # Dictionary to store contacts (name: phone number)
    
    def add_contact(self, name, phone):
        """Add a new contact to the phone book."""
        if name in self.contacts:
            print(f"Contact '{name}' already exists!")
            return
        self.contacts[name] = phone
        print(f"Contact '{name}' added successfully!")
    
    def delete_contact(self, name):
        """Delete a contact from the phone book."""
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found!")
    
    def list_contacts(self):
        """Display all contacts in the phone book."""
        if not self.contacts:
            print("Phone book is empty!")
        else:
            print("\nPhone Book Contacts:")
            print("-" * 30)
            for name, phone in self.contacts.items():
                print(f"Name: {name:15} Phone: {phone}")
            print("-" * 30)

def main():
    phone_book = PhoneBook()
    
    while True:
        print("\nPhone Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. List Contacts")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            phone_book.add_contact(name, phone)
            
        elif choice == '2':
            name = input("Enter contact name to delete: ")
            phone_book.delete_contact(name)
            
        elif choice == '3':
            phone_book.list_contacts()
            
        elif choice == '4':
            print("Thank you for using the Phone Book!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()