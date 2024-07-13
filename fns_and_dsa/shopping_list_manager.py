def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added")
        elif choice == "2":
            item = input("What would you like to remove?: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed.")
            else:
                print(f"{item} not found on list.")
        elif choice == '3':
            if shopping_list:
                print("Shopping List.")
                for item in shopping_list:
                    print(item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
display_menu()

if __name__ == "__main__":
    main()





