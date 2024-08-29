def counting_sort(arr):
    """
    Performs counting sort on a list of non-negative integers.

    Parameters:
    arr (list): The list of non-negative integers to be sorted.

    Returns:
    list: The sorted list.
    """
    if not arr:
        return arr  # Return empty array if input is empty

    # Find the maximum element in the array to determine the range
    max_val = max(arr)

    # Initialize count array with zeros
    count = [0] * (max_val + 1)

    # Store the count of each element in the input array
    for num in arr:
        count[num] += 1

    # Modify the count array by adding the previous counts (cumulative count)
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Create an output array that will be sorted
    output = [0] * len(arr)

    # Build the output array using the count array
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

if __name__ == "__main__":
    # Initial sample array
    sample_array = [4, 2, 2, 8, 3, 3, 1]
    print("Sample Array is:", sample_array)

    # Sort the sample array using counting sort
    sorted_array = counting_sort(sample_array)
    print("Sorted array:", sorted_array)

    # Prompt the user for input
    user_input = input("Enter the elements of the array (non-negative integers), separated by spaces: ")

    # Convert the user input string to a list of integers
    array = [int(x) for x in user_input.split()]

    # Sort the user-provided array using counting sort
    sorted_array = counting_sort(array)
    print("Sorted Array is:", sorted_array)
