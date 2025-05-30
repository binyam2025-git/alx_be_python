def simple_calculator():
    try:
       
       num1 = float(input("Enter the first number: "))
       num2 = float (input("Enter the second number: "))
       
       operation = input("Choose the operation (+, -, *, /): ")
      
       result = None # Initialize result variable
       
       # Perform the calculation using Match Case
       match operation:
           case '+':
               result = num1 + num2
           case '-':
               result = num1 - num2
           case '*':
               result = num1 * num2
           case '/':
               if num2 != 0:
                   result = num1 / num2
               else:
                   print("Cannot divide by zero.")
                   return 
           case _:
               print("Invalid operation. Please choose from +, -, *, /.")
               return 
       if result is not None:
           print(f"The result is {result}")
    except ValueError:
         print("Invalid Input. Please enter valid numbers.")
    except Exception as e:
         print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    simple_calculator()

