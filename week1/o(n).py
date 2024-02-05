def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def main():
    # Example array
    my_array = [3, 7, 1, 9, 5, 2, 8, 4, 6]

    # Search for the target value 5
    target_value = 5
    result = linear_search(my_array, target_value)

    if result != -1:
        print(f"Target {target_value} found at index {result}.")
    else:
        print(f"Target {target_value} not found in the array.")

if __name__ == "__main__":
    main()
