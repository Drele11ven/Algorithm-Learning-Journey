def merge_sort(arr):
    # Base case: if the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle point to divide the array into two halves
    mid = len(arr) // 2

    # Recursively call merge_sort on each half
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left , right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append the remaining elements in left, if any
    result.extend(left[i:])

    # Append the remaining elements in right, if any
    result.extend(right[j:])

    return result




if __name__ == "__main__":
    sample_array = [38, 27, 43, 3, 9, 82, 10]
    print("Sample Array is:", sample_array)
    
    sorted_array = merge_sort(sample_array)
    print("Sorted Array is:", sorted_array)
    
    # Prompt the user for input
    user_input = input("Enter the elements of the array, separated by spaces: ")
    
    # Split the input string by spaces and convert to a list of integers
    array = [int(x) for x in user_input.split()]
    sorted_array = merge_sort(array)
    print("Sorted Array is:", sorted_array)