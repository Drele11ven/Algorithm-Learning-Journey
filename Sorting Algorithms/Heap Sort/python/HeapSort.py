def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

if __name__ == "__main__":
    sample_array = [3, 6, 8, 10, 1, 2, 1]
    print("Sample Array is:", sample_array)

    sorted_array = heap_sort(sample_array)
    print("Sorted array:", sorted_array)

    user_input = input("Enter the elements of the array, separated by spaces: ")
    array = [int(x) for x in user_input.split()]

    sorted_array = heap_sort(array)
    print("Sorted Array is:", sorted_array)
