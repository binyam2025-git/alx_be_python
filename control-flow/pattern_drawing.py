def draw_square_pattern():
    try:
       size_str = input("Enter the size of the pattern:")
       size = int(size_str)
       
       if size <= 0:
           print("Please enter a positive integer for the pattern size.")
           return 
        
       current_row = 0

       while current_row < size:
           for _ in range(size):
               print("*", end="")
           print()
           current_row += 1
    except ValueError:
        print("Invalid input. Please enter a whole number.")
    except Exception as e:
        prin(f"An unexpected error occurred: {e}")
if __name__ == ""__main__"":
    draw_square_pattern()
