def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append the remaining elements, if any
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def main():
    # Example array
    my_array = [3, 7, 1, 9, 5, 2, 8, 4, 6]

    # Sort the array using merge sort
    sorted_array = merge_sort(my_array)

    print(f"Original Array: {my_array}")
    print(f"Sorted Array: {sorted_array}")

if __name__ == "__main__":
    main()
