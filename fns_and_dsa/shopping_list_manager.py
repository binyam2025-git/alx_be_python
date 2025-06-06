def display_menu():
	print("\n--- Shopping List Manager ---")
	print("1. Add Item")
	print("2. Remove Item")
	print("3. View List")
	print("4. Exit")
    #print("---------------------------")

def main():
	shopping_list = []

	while True:
		display_menu()
		choice = input("Enter your choice: ")

		if choice == '1':
			item_to_add = input("Enter the item to add: ").strip()
			if item_to_add:
				shopping_list.append(item_to_add)
				print(f"'{item_to_add}' has been added to the list.")
			else:
				print("Item name cannot be empty.")
		elif choice == '2':
			if not shopping_list:
				print("The shopping list is already empty. Nothing to remove.")
				continue

			item_to_remove = input("Enter the item to remove: ").strip()
			if item_to_remove:
				try:
					shopping_list.remove(item_to_remove)
					print(f"'{item_to_remove}' has been removed from the list.")
				except ValueError:
					print(f"'{item_to_remove}' not found in the list.")
			else:
				print("Item name cannot be empty.")
		elif choice == '3':
			print("\n--- Current Shopping List ---")
			if not shopping_list:
				print("The list is empty.")
			else:
				for i, item in enumerate(shopping_list, 1):
					print(f"{i}. {item}")
			print("---------------------------")

		elif choice == '4':

			print("Exiting Shopping List Manager. Goodbye!")
			break
		else:
			print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
