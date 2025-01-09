def display_menu():
    print("=======================")
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("=======================")
    
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            # Prompt for and add an item
            item = str(input("Enter the item to add: "))
            shopping_list.append(item)
        elif choice == 2:
            # Prompt for and remove an item
            item = str(input("Enter the item to remove. "))
            if shopping_list == []:
                print("The list is Empty.")
            elif item not in shopping_list:
                print(f"{item} is not in the Shopping list.")
            else:
                shopping_list.remove(item)
        elif choice == 3:
            # Display the shopping list
            print(shopping_list)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

