def fibonacci_sequence(n):
# Initialize the first two Fibonacci numbers
    fib_seq = [0, 1]
# Generate the Fibonacci sequence using a for loop
    for i in range(2, n):next_number = fib_seq[-1] + fib_seq[-2]
    fib_seq.append(next_number)
    # Return the sequence as a list
    return fib_seq[:n]
    # Example usage
n = 10
print(fibonacci_sequence(n))
