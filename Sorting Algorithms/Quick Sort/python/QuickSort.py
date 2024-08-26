def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    else:
        pivot = arr[-1] 
        left = [x for x in arr[:-1] if x <= pivot]  
        right = [x for x in arr[:-1] if x > pivot]  
        
        return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == "__main__":
    sample_array = [3, 6, 8, 10, 1, 2, 1]
    print("Sample Array is:", sample_array)
    
    sorted_array = quick_sort(sample_array)
    print("Sorted array:", sorted_array)

    user_input = input("Enter the elements of the array, separated by spaces :) ")
    
    array = [int(x) for x in user_input.split()]
    
    sorted_array = quick_sort(array)
    print("Sorted Array is:", sorted_array)
