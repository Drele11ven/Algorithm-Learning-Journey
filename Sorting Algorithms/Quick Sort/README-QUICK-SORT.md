# Quick Sort Algorithm

## Introduction

![Example Image](https://miro.medium.com/v2/resize:fit:1200/1*e-f1j1N3AIn5ZmS1uBWiKQ.png)

Quick Sort is a highly efficient sorting algorithm that uses a divide-and-conquer strategy to sort an array or list of elements. It is known for its fast performance on large datasets and works by selecting a 'pivot' element, partitioning the array around the pivot, and recursively sorting the subarrays.

## Origins and History

![Tony Hoare](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Sir_Tony_Hoare_IMG_5125.jpg/640px-Sir_Tony_Hoare_IMG_5125.jpg)
The Quick Sort algorithm was developed by Tony Hoare in 1959. It has since become one of the most popular sorting algorithms due to its average-case efficiency of O(n log n) and its in-place sorting capability, which reduces memory usage. Despite its worst-case time complexity of O(n^2), Quick Sort is often faster in practice than other O(n log n) algorithms like Merge Sort, due to its efficient memory cache performance.

## Pseudocode

```plaintext
QuickSort(array, low, high)
    if low < high
        pivot_index = Partition(array, low, high)
        QuickSort(array, low, pivot_index - 1)  // Recursively sort the left subarray
        QuickSort(array, pivot_index + 1, high) // Recursively sort the right subarray

Partition(array, low, high)
    pivot = array[high]
    i = low - 1
    for j = low to high - 1
        if array[j] <= pivot
            i = i + 1
            swap array[i] with array[j]
    swap array[i + 1] with array[high]
    return (i + 1)
```

## Explanation

Quick Sort works by selecting a 'pivot' element from the array and partitioning the other elements into two subarrays based on whether they are less than or greater than the pivot. The subarrays are then sorted recursively. This process continues until the base case of an empty or single-element subarray is reached, which is inherently sorted.

- **Step 1:** Choose a pivot element from the array (commonly the last element).
- **Step 2:** Partition the array into two subarrays: elements less than or equal to the pivot and elements greater than the pivot.
- **Step 3:** Recursively apply the same process to the left and right subarrays.
- **Step 4:** Combine the sorted subarrays to produce the final sorted array.

## Example

Let's consider an example of sorting an array `[38, 27, 43, 3, 9, 82, 10]` using Quick Sort:

1. **Choose Pivot:** Select the last element `10` as the pivot.
2. **Partition:** Rearrange elements so that all elements less than `10` come before it, and all elements greater come after it.
3. **Recursive Sort:** Recursively apply Quick Sort to the subarrays `[3, 9]` and `[38, 27, 43, 82]`.
4. **Combine Results:** Combine the results to produce the final sorted array.

## Expected Result

The sorted array after applying Quick Sort on `[38, 27, 43, 3, 9, 82, 10]` will be:

`[3, 9, 10, 27, 38, 43, 82]`

## Conclusion

Quick Sort is a fast, in-place sorting algorithm with an average-case time complexity of O(n log n). It is widely used for its performance advantages and simplicity. While its worst-case complexity is O(n^2), this is rare with good pivot selection strategies, such as using the median or a random pivot.

Feel free to explore the code and contribute to its improvement. Happy coding!

## References

- [Wikipedia: Quick Sort](https://en.wikipedia.org/wiki/Quicksort)
- [GeeksforGeeks: Quick Sort](https://www.geeksforgeeks.org/quick-sort/)
- [Khan Academy: Quick Sort](https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/overview-of-quick-sort)
