def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == "__main__":
    # Define a sorted array and target value
    predefined_array = [1, 5, 8, 12, 23, 34, 56, 78]
    predefined_target = 23

    # Print the predefined array and target value
    print("Predefined Array:", predefined_array)
    print("Searching for target:", predefined_target)

    # Perform binary search on the predefined array
    index = binary_search(predefined_array, predefined_target)

    if index !=-1:
        print(f"Target value {predefined_target} found at index {index}.")
    else:
        print(f"Target value {predefined_target} not found in the predefined array.")

    # Prompt the user for input
    user_input = input("Enter a sorted array of integers separated by spaces: ")
    target = int(input("Enter the target value to search for: "))

    # Convert user input into a list of integers
    user_array = list(map(int, user_input.split()))

    # Print the user-provided array and target value
    print("User-provided Array:", user_array)
    print("Searching for target:", target)

    # Perform binary search on the user-provided array
    index = binary_search(user_array, target)

    if index != -1:
        print(f"Target value {target} found at index {index}.")
    else:
        print(f"Target value {target} not found in the user-provided array.")
