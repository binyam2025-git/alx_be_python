"""
polymorphism_demo.py

This script demonstrates polymorphism and method overriding in Python
by defining a base class 'Shape' and derived classes 'Rectangle' and 'Circle'.

Classes:
    Shape: A base class with a placeholder area() method.
    Rectangle: A derived class of Shape, representing a rectangle.
    Circle: A derived class of Shape, representing a circle.
"""

import math

class Shape:
    """
    Base class for geometric shapes.

    Defines an 'area' method that is intended to be overridden by derived classes.
    """
    def area(self):
        """
        Calculates the area of the shape.
        This method must be overridden by concrete shape classes.

        Raises:
            NotImplementedError: If the method is not overridden by a derived class.
        """
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Rectangle(Shape):
    """
    Represents a rectangle, inheriting from Shape.

    Attributes:
        length (int or float): The length of the rectangle.
        width (int or float): The width of the rectangle.
    """
    def __init__(self, length: float, width: float):
        """
        Initializes a new Rectangle instance.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area method from the Shape base class.
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """
    Represents a circle, inheriting from Shape.

    Attributes:
        radius (int or float): The radius of the circle.
    """
    def __init__(self, radius: float):
        """
        Initializes a new Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Overrides the area method from the Shape base class.
        Calculates the area of the circle using the formula π * radius².

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

# Example usage (for direct testing, though main.py will be used for official testing):
if __name__ == "__main__":
    print("--- Testing Polymorphism Demo directly ---")

    try:
        # Attempting to create a generic Shape and call area (should raise error)
        # generic_shape = Shape()
        # print(generic_shape.area())
        pass # Commented out as per task, but good for demonstrating NotImplementedError
    except NotImplementedError as e:
        print(f"Caught expected error: {e}")

    # Create instances of derived shapes
    my_rectangle = Rectangle(10, 5)
    my_circle = Circle(7)

    # Demonstrate polymorphic behavior
    shapes_list = [my_rectangle, my_circle]

    for shape_obj in shapes_list:
        # The 'area' method is called on a 'Shape' object, but Python
        # dispatches to the correct overridden method based on the
        # actual type of 'shape_obj' (Rectangle or Circle).
        print(f"The area of the {shape_obj.__class__.__name__} is: {shape_obj.area()}")

    print("--- Direct testing complete ---")
