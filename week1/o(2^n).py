def fibonacci_naive_recursive(n):
    if n <= 1:
        return n
    else:
        # Recursive calls with exponential growth
        return fibonacci_naive_recursive(n - 1) + fibonacci_naive_recursive(n - 2)

def main():
    # Calculate the 8th Fibonacci number
    result = fibonacci_naive_recursive(8)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
