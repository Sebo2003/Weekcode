def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if the target is at the middle
        if arr[mid] == target:
            return mid
        # If the target is smaller, search the left half
        elif arr[mid] > target:
            high = mid - 1
        # If the target is larger, search the right half
        else:
            low = mid + 1

    # If the target is not in the array
    return -1

def main():
    # Example sorted array
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Search for the target value 6
    target_value = 6
    result = binary_search(sorted_array, target_value)

    if result != -1:
        print(f"Target {target_value} found at index {result}.")
    else:
        print(f"Target {target_value} not found in the array.")

if __name__ == "__main__":
    main()

#Set is cut in half each time.
#n/2, n/4, n/8, n/16, ect
#Since its in half each time, operation is performed log (n) times
#                                                       2