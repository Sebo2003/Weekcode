def example_function(m, n):
    # Operation 1: O(m)
    for i in range(m):
        print(f"Operation 1 - Iteration {i}")

    # Operation 2: O(n^2)
    for i in range(n):
        for j in range(n):
            print(f"Operation 2 - Iteration {i}, {j}")

# Example usage
example_function(3, 4)
