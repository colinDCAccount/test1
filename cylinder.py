"""Volume and area of cylinder, with exceptions.
This is the starter version, without exceptions.
The functions return a negative value if the height is negative.

TPRG 2131 Fall 202x Test 1
"""

from math import pi

def volume_cylinder(diameter, height):
    """Volume of a cylinder given diameter and height."""
    if height < 0:
        raise ValueError("height must be non-negative")
    return pi * (diameter / 2.0) ** 2 * height

def area_cylinder(diameter, height):
    """Surface area of a cylinder given diameter and height."""
    if height < 0:
        raise ValueError("height must be non-negative")
    radius = diameter / 2.0
    return 2.0 * pi * radius * (height + radius)  # simplified

if __name__ == "__main__":
    try:
        while True:
            dia = float(input("\nDiameter? "))
            high = float(input("Height? "))
            print("The volume is", volume_cylinder(dia, high))
            print("The area is", area_cylinder(dia, high))
    except ValueError as e:
        # Covers negative height and any non-numeric parse errors
        # (message explains the negative-height case as required)
        print("Please enter a positive value for height.")
    except KeyboardInterrupt:
        print("\nGoodbye!")

