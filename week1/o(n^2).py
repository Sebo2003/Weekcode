def quadratic_algorithm(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n):
            # Some operation (e.g., comparison) on each pair of elements
            # This could be any operation that contributes to the time complexity
            result = arr[i] > arr[j]

    return result

def main():
    # Example array
    my_array = [3, 7, 1, 9, 5, 2, 8, 4, 6]

    # Perform the quadratic algorithm
    result = quadratic_algorithm(my_array)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()