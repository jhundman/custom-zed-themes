# Example Python Script to Showcase ZED IDE Theme Styling

"""
This script demonstrates various Python syntax elements:
- Single and multi-line comments
- Function definitions with arguments and return values
- Conditional statements and loops
- Class definitions, inheritance, and method overriding
- List comprehensions and lambda functions
"""

# Import statement
import math


# Function definition with a docstring
def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * radius**2


# Class definitions and inheritance
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return calculate_area(self.radius)


# Main function showcasing a conditional, loop, and list comprehension
def main():
    shapes = [Circle(3), Circle(5)]

    bools = True and False

    # List comprehension and lambda fuction
    areas = list(map(lambda x: x.area(), shapes))

    for i, area in enumerate(areas):
        print(f"Area of {shapes[i].name} with radius {shapes[i].radius}: {area:.2f}")


# Inline comment about the entry point of the script
if __name__ == "__main__":
    main()
