def counting_sort(arr, exp):
    """
    Perform Counting Sort based on the digit represented by exp (10^i).
    
    Parameters:
    arr (list): The list of elements to be sorted based on the current digit.
    exp (int): The exponent representing the current digit position (1, 10, 100, etc.).
    
    Returns:
    list: A new list with elements sorted based on the current digit.
    """
    n = len(arr)
    output = [0] * n  # Output array to store sorted elements
    count = [0] * 10  # Count array to store the count of each digit (0-9)

    # Calculate the count of elements based on the current digit
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update the count array to store the position of each digit in the output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr[] contains sorted numbers
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    """
    Perform Radix Sort and return a sorted array.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    list: A new list with sorted elements.
    """
    # Find the maximum number to determine the number of digits
    max_value = max(arr)
    exp = 1  # Start with the least significant digit

    # Perform counting sort for each digit
    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr


# Example usage
if __name__ == "__main__":
    sample_array = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Sample Array is:", sample_array)
    
    # Using the radix_sort function to get a new sorted array
    sorted_array = radix_sort(sample_array)
    print("Sorted array:", sorted_array)

    # Prompt the user for input
    user_input = input("Enter the elements of the array, separated by spaces: ")
    
    # Split the input string by spaces and convert to a list of integers
    array = [int(x) for x in user_input.split()]
    
    # Get the sorted array and print it
    sorted_array = radix_sort(array)
    print("Sorted Array is:", sorted_array)
