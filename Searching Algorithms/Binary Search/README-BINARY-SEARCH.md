# Binary Search Algorithm

## Introduction

Binary Search is an efficient algorithm for finding a target value within a sorted array. It works by repeatedly dividing the search interval in half. If the target value is less than the item in the middle of the interval, the search continues on the lower half, or if it is greater, on the upper half. This process is continued until the target value is found or the interval is empty.

![Binary Search Diagram]()

## Origins and History

![John Mauchly]()

Binary Search was first described by John Mauchly in 1946 as part of the ENIAC computer's design. It is an improvement over linear search algorithms, which are less efficient for large datasets. Binary Search leverages the fact that the array is sorted, allowing it to achieve a time complexity of O(log n), making it significantly faster than linear search algorithms.

## Pseudocode

```plaintext
BinarySearch(array, target)
    low = 0
    high = length(array) - 1

    while low <= high
        mid = (low + high) / 2
        if array[mid] == target
            return mid
        else if array[mid] < target
            low = mid + 1
        else
            high = mid - 1

    return -1  // Target not found
```

## Explanation

Binary Search works by repeatedly dividing the search range in half. The steps are as follows:

1. **Initialization:** Set the initial search range with `low` and `high` pointers at the start and end of the array.
2. **Find the Middle:** Calculate the middle index of the current search range.
3. **Compare Values:** Compare the target value with the middle element.
   - If the middle element is equal to the target, the search is successful, and the index of the middle element is returned.
   - If the target value is less than the middle element, narrow the search range to the lower half.
   - If the target value is greater than the middle element, narrow the search range to the upper half.
4. **Repeat:** Continue the process until the target is found or the search range is empty.
5. **Not Found:** If the search range becomes empty (i.e., `low` exceeds `high`), the target is not present in the array, and `-1` is returned.

## Example

Consider searching for the value `23` in the sorted array `[1, 5, 8, 12, 23, 34, 56, 78]` using Binary Search:

1. **Initial Range:** `low = 0`, `high = 7`
2. **Middle Element:** `(0 + 7) / 2 = 3` (element `12`)
   - `23` > `12`, so search the upper half (`low = 4`, `high = 7`)
3. **Middle Element:** `(4 + 7) / 2 = 5` (element `34`)
   - `23` < `34`, so search the lower half (`low = 4`, `high = 4`)
4. **Middle Element:** `(4 + 4) / 2 = 4` (element `23`)
   - `23` == `23`, so the target is found at index `4`.

### Detailed Steps:

1. **First Comparison:** Middle element is `12`, target is greater, adjust range.
2. **Second Comparison:** Middle element is `34`, target is smaller, adjust range.
3. **Third Comparison:** Middle element is `23`, target is found.

## Expected Result

For the sorted array `[1, 5, 8, 12, 23, 34, 56, 78]`, searching for `23` using Binary Search will return the index `4`.

## Conclusion

Binary Search is a highly efficient algorithm for finding an element in a sorted array, with a time complexity of O(log n). It is widely used due to its speed and simplicity, making it a valuable tool for searching operations in various applications.

Feel free to explore the code and contribute to its improvement. Happy searching!

## References

- [Wikipedia: Binary Search](https://en.wikipedia.org/wiki/Binary_search_algorithm)
- [GeeksforGeeks: Binary Search](https://www.geeksforgeeks.org/binary-search/)
- [Khan Academy: Binary Search](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search)
