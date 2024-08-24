def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Flag to check if any swap happened
        swapped = False
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped
        # by inner loop, then break
        if not swapped:
            break
    return arr
# by using __name__ == "__main__" condition
#later we can use this module too

if __name__ == "__main__":
    sample_array = [64, 32, 25, 12, 22, 11, 99]
    print("sample Array is : ", sample_array)
    sorted_array = bubble_sort(sample_array)
    print("Sorted Array is : ", sorted_array)
    # Prompt the user for input
    user_input = input("Enter the elements of the array, separated by spaces: for your test :) ")
    # Split the input string by commas and convert to a list
    array = [int(x) for x in user_input.split(' ')]
    sorted_array = bubble_sort(array)
    print("Sorted Array is : ", sorted_array)