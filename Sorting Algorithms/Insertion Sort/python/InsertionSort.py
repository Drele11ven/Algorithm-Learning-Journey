def insertion_sort(arr):
    """
    Sorts an array in ascending order using the insertion sort algorithm.
    
    Parameters:
    arr (list): A list of comparable elements (e.g., integers).

    Returns:
    list: A sorted list in ascending order.
    """
    # Iterate from the second element (index 1) to the end of the array
    for i in range(1, len(arr)):  
        key = arr[i]  # Store the current element to be compared
        j = i - 1  # Initialize j to point to the element before the current one

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element one position to the right
            j = j - 1  # Move j one position to the left
        
        # Place the key in its correct position in the sorted subarray
        arr[j + 1] = key

    return arr  # Return the sorted array


if __name__ == "__main__":
    # Initial sample array
    sample_array = [3, 6, 8, 10, 1, 2, 1]
    print("Sample Array is:", sample_array)

    # Sort the sample array using insertion sort
    sorted_array = insertion_sort(sample_array)
    print("Sorted array:", sorted_array)

    # Prompt the user for input
    user_input = input("Enter the elements of the array, separated by spaces: ")

    # Convert the user input string to a list of integers
    array = [int(x) for x in user_input.split()]

    # Sort the user-provided array using insertion sort
    sorted_array = insertion_sort(array)
    print("Sorted Array is:", sorted_array)
