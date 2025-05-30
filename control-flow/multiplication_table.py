def generate_multiplication_table():
    
    try:
        number = int(input("Enter a number to see its multiplication table: "))

        print(f"Multiplication table for {number}:")
        
        for i in range(1, 11):
            prodcut = number * i 
            print(f"{number} * {i} = {product}")

    except ValueError:
        print("Invalid input. Please enter a whole number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    generate_multiplication_table()
