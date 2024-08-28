def heapify(arr, n, i):
    """
    Maintains the heap property for a subtree rooted at index i.

    Parameters:
    arr (list): The list representation of the heap.
    n (int): The size of the heap.
    i (int): The index of the root of the subtree.

    Returns:
    None
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If left child exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # If right child exists and is greater than largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

def heap_sort(arr):
    """
    Performs heap sort on a list.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    n = len(arr)  # Size of the heap

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (maximum value) with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

    return arr  # Return the sorted array

if __name__ == "__main__":
    # Initial sample array
    sample_array = [3, 6, 8, 10, 1, 2, 1]
    print("Sample Array is:", sample_array)

    # Sort the sample array using heap sort
    sorted_array = heap_sort(sample_array)
    print("Sorted array:", sorted_array)

    # Prompt the user for input
    user_input = input("Enter the elements of the array, separated by spaces: ")

    # Convert the user input string to a list of integers
    array = [int(x) for x in user_input.split()]

    # Sort the user-provided array using heap sort
    sorted_array = heap_sort(array)
    print("Sorted Array is:", sorted_array)
