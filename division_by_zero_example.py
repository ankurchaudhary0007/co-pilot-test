def calculate_ratio(a, b):
    """
    Returns the ratio a / b. Possible division by zero if b is 0.
    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Denominator 'b' must not be zero.")
    return a / b

# Example usages
print(calculate_ratio(10, 2))   # Output: 5.0
print(calculate_ratio(5, 0))    # Raises ZeroDivisionError

# Another example with a list of denominators
for denom in [3, 2, 1, 0, -1]:
    print(f"10 / {denom} = {calculate_ratio(10, denom)}")
