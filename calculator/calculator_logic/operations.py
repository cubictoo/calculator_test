def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the division of a by b.
    Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

import math

def square_root(a):
    """Returns the square root of a.
    Raises ValueError if a is negative."""
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)

def power(base, exponent):
    """Returns base raised to the power of exponent."""
    return math.pow(base, exponent)

def log_natural(a):
    """Returns the natural logarithm (base e) of a.
    Raises ValueError if a is not positive."""
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return math.log(a)

def log_base10(a):
    """Returns the base-10 logarithm of a.
    Raises ValueError if a is not positive."""
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return math.log10(a)

def sin_degrees(angle_degrees):
    """Returns the sine of an angle given in degrees."""
    return math.sin(math.radians(angle_degrees))

def cos_degrees(angle_degrees):
    """Returns the cosine of an angle given in degrees."""
    return math.cos(math.radians(angle_degrees))

def tan_degrees(angle_degrees):
    """Returns the tangent of an angle given in degrees."""
    # Optional: Add check for angles like 90, 270 where tan is undefined
    # For simplicity, relying on math.tan to handle large values.
    if (angle_degrees % 180 == 90): # Checks for 90, 270, etc.
        # Tan is undefined for these angles. We can return infinity or raise an error.
        # Python's math.tan returns a very large number for these instead of an error.
        # For a more user-friendly calculator, explicit handling might be better.
        # However, for now, let's align with math.tan's behavior for simplicity.
        pass # Let math.tan handle it.
    return math.tan(math.radians(angle_degrees))
