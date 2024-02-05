def generate_permutations(elements):
    if len(elements) == 0:
        return [[]]

    permutations = []
    for i in range(len(elements)):
        remaining_elements = elements[:i] + elements[i+1:]
        for perm in generate_permutations(remaining_elements):
            permutations.append([elements[i]] + perm)

    return permutations

def main():
    # Example set of elements
    my_set = [1, 2, 3]

    # Generate all permutations
    result = generate_permutations(my_set)

    print("All Permutations:")
    for perm in result:
        print(perm)

if __name__ == "__main__":
    main()
