def fibonacci(n):
    """Generate Fibonacci sequence up to n numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Example usage
if __name__ == "__main__":
    result = fibonacci(10)
    print("Fibonacci sequence (10 numbers):", result)
