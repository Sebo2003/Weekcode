# Function to access an element in a list by index
def access_element(my_list, index):
    return my_list[index]

def main():
    # Create a list of integers
    my_list = [1, 4, 7, 10, 13]

    # Access the element at index 2 (third element)
    result = access_element(my_list, 2)

    # Print the result
    print(f"Element at index 2: {result}")

if __name__ == "__main__":
    main()