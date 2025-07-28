def sum_natural_numbers(n):
    """
    Returns the sum of the first n natural numbers.
    Formula used: n * (n + 1) // 2
    """
    return n * (n + 1) // 2

# Example usage:
number = int(input("Enter a positive integer: "))
if number > 0:
    total = sum_natural_numbers(number)
    print(f"The sum of the first {number} natural numbers is: {total}")
else:
    print("Please enter a positive integer.")
