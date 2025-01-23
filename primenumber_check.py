def is_prime(n):
# Validate that the input is a positive integer greater than 1
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input must be an integer greater than 1")
        # Check for factors other than 1 and n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# Example usage
try:
    number = 7
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
except ValueError as e:
    print(e)