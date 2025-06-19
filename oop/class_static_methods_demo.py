class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of a and b (no class or instance reference needed)."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Prints the class attribute and returns the product of a and b."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
