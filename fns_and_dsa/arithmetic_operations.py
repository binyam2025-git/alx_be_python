def perform_operation(num1, num2, operation):
    """
    Performs a basic arithmetic operation based on the given numbers and operation string.

    Args:
        num1 (int or float): The first number.
        num2 (int or float): The second number.
        operation (str): The string representing the operation ('add', 'subtract', 'multiply', 'divide').

    Returns:
        int or float or str: The result of the operation, or an error message if
                             the operation is invalid or division by zero occurs.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

# --- Example Usage (Optional - for testing purposes) ---
if __name__ == "__main__":
    print(f"10 + 5 = {perform_operation(10, 5, 'add')}")
    print(f"10 - 5 = {perform_operation(10, 5, 'subtract')}")
    print(f"10 * 5 = {perform_operation(10, 5, 'multiply')}")
    print(f"10 / 5 = {perform_operation(10, 5, 'divide')}")
    print(f"10 / 0 = {perform_operation(10, 0, 'divide')}")
    print(f"5 + 'a' = {perform_operation(5, 'a', 'add')}") # Example of type error (Python handles this with TypeError)
    print(f"10 % 3 = {perform_operation(10, 3, 'modulo')}") # Example of invalid operation
