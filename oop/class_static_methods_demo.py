"""
class_static_methods_demo.py

This script defines a Calculator class to demonstrate the usage and differences
between static methods and class methods in Python.

Classes:
    Calculator: A class that performs arithmetic operations using a static method
                and a class method.
"""

class Calculator:
    """
    A class that demonstrates static and class methods for arithmetic operations.

    Class Attributes:
        calculation_type (str): Describes the type of calculations performed.
    """
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        A static method that returns the sum of two numbers.
        It does not have access to the class (cls) or instance (self).

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        A class method that returns the product of two numbers.
        It has access to the class itself (cls), which allows it to
        access class attributes like 'calculation_type'.

        Args:
            cls (type): The class itself (automatically passed).
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of a and b.
        """
        # Accessing a class attribute using the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Example usage (for direct testing, though main.py will be used for official testing):
if __name__ == "__main__":
    print("--- Testing Calculator Class directly ---")

    # Using the static method (can be called on the class itself without an instance)
    direct_sum_result = Calculator.add(20, 10)
    print(f"Direct sum (static method): {direct_sum_result}")

    # Using the class method (can also be called on the class itself)
    direct_product_result = Calculator.multiply(20, 10)
    print(f"Direct product (class method): {direct_product_result}")

    # You can also call them on an instance, though it's less common for static/class methods
    # instance_calculator = Calculator()
    # instance_sum = instance_calculator.add(3, 2)
    # print(f"Instance sum (static method): {instance_sum}")
    # instance_product = instance_calculator.multiply(3, 2)
    # print(f"Instance product (class method): {instance_product}")

    print("--- Direct testing complete ---")
