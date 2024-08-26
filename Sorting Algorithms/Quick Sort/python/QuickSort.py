def quick_sort(arr):
    """
    Perform Quick Sort and return a sorted array.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    list: A new list with sorted elements.
    """
    # Base case: If the list is empty or has one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Recursive case: Perform quick sort
    else:
        pivot = arr[-1]  # Choosing the last element as the pivot
        left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to pivot
        right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot
        
        # Recursively apply quick sort to left and right subarrays and combine with pivot
        return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
if __name__ == "__main__":
    sample_array = [3, 6, 8, 10, 1, 2, 1]
    print("Sample Array is:", sample_array)
    
    # Using the modified quick_sort function to get a new sorted array
    sorted_array = quick_sort(sample_array)
    print("Sorted array:", sorted_array)

    # Prompt the user for input
    user_input = input("Enter the elements of the array, separated by spaces:) ")
    
    # Split the input string by spaces and convert to a list of integers
    array = [int(x) for x in user_input.split()]
    
    # Get the sorted array and print it
    sorted_array = quick_sort(array)
    print("Sorted Array is:", sorted_array)
