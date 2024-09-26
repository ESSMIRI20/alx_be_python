
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            a = input(("Enter the item to add:"))
            shopping_list.append(a)
        elif choice == '2':
            a = input(("what's the item you need to remove it :"))
            shopping_list.remove(a)
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# if __name__ == "__main__":
    main()