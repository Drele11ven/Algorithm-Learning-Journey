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
    #Define a sorted array and target value
    array = [1, 5, 8, 12, 23, 34, 56, 78]
    target = 23

    print(f"Array: {array}")
    print(f"Target: {target}")

    index = binary_search(array, target)

    if index != -1:
        print(f"Target value {target} found at index {index}.")
    else:
        print(f"Target value {target} not found in the array.")
