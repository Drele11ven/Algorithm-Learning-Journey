# Counting Sort Algorithm

## Introduction

Counting Sort is a non-comparison-based sorting algorithm that sorts elements by counting the occurrences of each unique value in the input data. It then uses this information to determine the position of each element in the sorted output. Unlike comparison-based sorting algorithms, Counting Sort has a time complexity of O(n + k), where `n` is the number of elements in the input array and `k` is the range of the input. This makes Counting Sort highly efficient for sorting data with a small range of integer keys. 

Counting Sort is particularly well-suited for applications where the range of potential items in the input data is known and not significantly larger than the number of items to be sorted. However, it is not an in-place sorting algorithm, as it requires additional storage proportional to the range of the input data. Despite this, Counting Sort is stable and performs well when the range of the input data is not significantly greater than the number of elements.

## Origins and History

Counting Sort was developed as a linear-time sorting algorithm to provide a more efficient alternative to traditional comparison-based algorithms like Quick Sort and Merge Sort for specific use cases, especially when the input data range is limited.

## Pseudocode

```plaintext
CountingSort(array, maxVal)
    # Initialize count array with all zeros
    count = array of zeros with length maxVal + 1

    # Store the count of each element
    for num in array
        count[num] = count[num] + 1

    # Store the cumulative sum of counts
    for i from 1 to maxVal
        count[i] = count[i] + count[i - 1]

    # Find the index of each element of the original array in count array
    # and place the elements in output array
    output = array of zeros with length of array
    for i from length of array - 1 downto 0
        output[count[array[i]] - 1] = array[i]
        count[array[i]] = count[array[i]] - 1

    return output
```

## Explanation

Counting Sort works by counting the frequency of each element in the input array and using this frequency count to calculate the position of each element in the sorted output array. The algorithm involves three main steps:

1. **Counting the Elements:** The algorithm first creates a count array to store the frequency of each unique element in the input array. The index of the count array represents the element value, and the value at each index represents the frequency of that element.
    
2. **Calculating Cumulative Counts:** Next, the algorithm calculates the cumulative counts to determine the position of each element in the sorted array. The cumulative count is obtained by iterating through the count array and adding the count of the current element to the count of the previous element.
    
3. **Placing Elements in Sorted Order:** Finally, the algorithm iterates through the input array in reverse order, uses the cumulative count to determine the correct position of each element in the output array, and places the element accordingly. This step also decrements the count in the count array to handle duplicate elements correctly.

## Example

Let's sort an array `[4, 2, 2, 8, 3, 3, 1]` using Counting Sort:

1. **Initial Array:** `[4, 2, 2, 8, 3, 3, 1]`
    
2. **Count Array:** 
   - After counting elements: `[0, 1, 2, 2, 1, 0, 0, 0, 1]`
   
3. **Cumulative Count Array:** 
   - After calculating cumulative counts: `[0, 1, 3, 5, 6, 6, 6, 6, 7]`

4. **Placing Elements in Sorted Order:**
   - Place each element from the input array into its correct position in the output array using the cumulative count.

5. **Final Sorted Array:** `[1, 2, 2, 3, 3, 4, 8]`

The array is now sorted in ascending order.

## Conclusion

Counting Sort is an efficient sorting algorithm for datasets where the range of potential values is known and relatively small. Its linear time complexity makes it a powerful tool for sorting integers or other data types that can be mapped to a finite range of integers.
