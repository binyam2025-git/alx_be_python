def draw_square_pattern():
    """
    Prompts the user for a positive integer (size) and prints a square
    pattern of asterisks of that size using nested loops.
    Handles invalid input gracefully.
    """
    try:
        # 1. Checks for user input: Prompt and initial type conversion
        size_str = input("Enter the size of the pattern: ")
        size = int(size_str) # Attempts to convert to int. Will raise ValueError if not a valid integer.

        # 1. Checks for user input: Validate if the input is a POSITIVE integer
        if size <= 0:
            print("Please enter a positive integer for the pattern size.")
            return # Exit the function if input is not positive

        current_row = 0
        # 2. Checks for existence of while loop: Outer loop controlling rows
        while current_row < size:
            # Inner for loop: prints asterisks for the current row
            # It iterates 'size' times to print 'size' asterisks
            for _ in range(size):
                print("*", end="") # Print asterisk without moving to a new line

            print() # After printing all asterisks for a row, move to the next line
            current_row += 1 # Increment the row counter for the while loop

    except ValueError:
        # Handles cases where the user inputs something that isn't a whole number
        print("Invalid input. Please enter a whole number.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# This standard idiom ensures the function runs only when the script is executed directly
if __name__ == "__main__":
    draw_square_pattern()
