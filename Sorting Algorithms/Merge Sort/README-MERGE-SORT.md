# Merge Sort Algorithm

## Introduction

![Example Image](https://miro.medium.com/v2/resize:fit:661/1*7Kox4Bll0Ddvb0td1tiXsg.png)

Merge Sort is a popular sorting algorithm that uses a divide-and-conquer approach to sort an array or list of elements. It is known for its efficiency and stable sorting, which means it maintains the relative order of equal elements. The algorithm divides the array into two halves, recursively sorts each half, and then merges the two sorted halves back together.

## Origins and History

The Merge Sort algorithm was invented by John von Neumann in 1945. It is one of the earliest sorting algorithms and has laid the foundation for various modern-day sorting algorithms. Merge Sort's divide-and-conquer approach was revolutionary at the time, and it remains a fundamental algorithm in computer science today due to its reliable performance, especially for large datasets.

## Pseudocode
```
MergeSort(array)
    if length of array <= 1
        return array

    mid = length of array / 2
    leftHalf = MergeSort(array[0:mid])
    rightHalf = MergeSort(array[mid:length of array])

    return Merge(leftHalf, rightHalf)

Merge(left, right)
    result = empty array
    while left is not empty and right is not empty
        if left[0] <= right[0]
            append left[0] to result
            remove left[0] from left
        else
            append right[0] to result
            remove right[0] from right
    while left is not empty
        append left[0] to result
        remove left[0] from left
    while right is not empty
        append right[0] to result
        remove right[0] from right

    return result
```

## Explanation

Merge Sort works by recursively dividing the unsorted list into smaller sublists until each sublist contains only one element (which is inherently sorted). Then, it repeatedly merges sublists to produce new sorted sublists until only one sorted sublist remains.

- **Step 1:** Divide the unsorted list into `n` sublists, each containing one element.
- **Step 2:** Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

The merging process involves comparing the smallest elements of each sublist, taking the smallest among them, and appending it to the result list. This process is repeated until all elements from both sublists are used.

## Example

Let's consider an example of sorting an array `[38, 27, 43, 3, 9, 82, 10]` using Merge Sort:

1. **Divide:** The array is recursively divided into subarrays:
   - `[38, 27, 43, 3]` and `[9, 82, 10]`
   - `[38, 27]` and `[43, 3]` and `[9]` and `[82, 10]`
   - `[38]`, `[27]`, `[43]`, `[3]`, `[9]`, `[82]`, `[10]`

2. **Merge:** The divided arrays are merged in a sorted manner:
   - Merge `[38]` and `[27]` to get `[27, 38]`
   - Merge `[43]` and `[3]` to get `[3, 43]`
   - Merge `[82]` and `[10]` to get `[10, 82]`

3. Continue merging:
   - Merge `[27, 38]` and `[3, 43]` to get `[3, 27, 38, 43]`
   - Merge `[9]` and `[10, 82]` to get `[9, 10, 82]`

4. **Final Merge:** Merge `[3, 27, 38, 43]` and `[9, 10, 82]` to get `[3, 9, 10, 27, 38, 43, 82]`

## Expected Result

The sorted array after applying Merge Sort on `[38, 27, 43, 3, 9, 82, 10]` will be:

[3, 9, 10, 27, 38, 43, 82]

## Conclusion

Merge Sort is an efficient, stable, and well-established sorting algorithm with a time complexity of `O(n log n)` in the worst, average, and best cases. It is particularly useful for sorting large datasets and has been widely used in various applications where stable sorting is required.

Feel free to explore the code and contribute to its improvement. Happy coding!

## References

- [Wikipedia: Merge Sort](https://en.wikipedia.org/wiki/Merge_sort)
- [GeeksforGeeks: Merge Sort](https://www.geeksforgeeks.org/merge-sort/)
- [Khan Academy: Merge Sort](https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort)