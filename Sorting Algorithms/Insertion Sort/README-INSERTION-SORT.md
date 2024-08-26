# Insertion Sort Algorithm

## Introduction

![Example Image](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

Insertion Sort is a simple and intuitive sorting algorithm that builds the final sorted array one element at a time. It is often compared to the way one might sort playing cards in their hands. While not the most efficient for large datasets, Insertion Sort is efficient for small datasets or mostly sorted arrays, with a time complexity of O(n^2) in the worst case.

## Origins and History

![John von Neumann](https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/VonNeumann-Silhouette.png/640px-VonNeumann-Silhouette.png)

Though the specific origins of the Insertion Sort algorithm are unclear, the method is closely related to the concept of sequential processing, which has been a part of algorithmic thinking since the early days of computing. It is particularly useful in scenarios where small, mostly sorted arrays require fine-tuning.

## Pseudocode

```plaintext
InsertionSort(array)
    for i = 1 to array.length - 1
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
```

## Explanation

Insertion Sort iterates through the list, growing the sorted portion behind the current index by inserting each new element into its correct position within the sorted portion.

- **Step 1:** Start from the second element, assume the first element is already sorted.
- **Step 2:** Compare the current element with the elements in the sorted portion and shift all larger elements one position to the right.
- **Step 3:** Insert the current element into its correct position.
- **Step 4:** Repeat this process for all elements in the array until the array is fully sorted.

## Example

Let's consider an example of sorting an array `[12, 11, 13, 5, 6]` using Insertion Sort:

1. **Initial Array:** `[12, 11, 13, 5, 6]`
2. **Step 1:** Start with `11`. Since `11` is less than `12`, move `12` one position to the right and insert `11` in the first position. Array becomes `[11, 12, 13, 5, 6]`.
3. **Step 2:** `13` is already in the correct position. No changes are needed.
4. **Step 3:** Move `5` to the beginning by shifting `11, 12, 13` to the right. Array becomes `[5, 11, 12, 13, 6]`.
5. **Step 4:** Move `6` into its correct position. Shift `11, 12, 13` right. Array becomes `[5, 6, 11, 12, 13]`.

## Expected Result

The sorted array after applying Insertion Sort on `[12, 11, 13, 5, 6]` will be:

`[5, 6, 11, 12, 13]`

## Conclusion

Insertion Sort is a straightforward sorting algorithm with an average and worst-case time complexity of O(n^2). While not suitable for large datasets, it excels in sorting small or mostly sorted arrays. It is also an in-place and stable sort, making it useful in certain applications where memory usage and data consistency are important.

Feel free to explore the code and contribute to its improvement. Happy coding!

## References

- [Wikipedia: Insertion Sort](https://en.wikipedia.org/wiki/Insertion_sort)
- [GeeksforGeeks: Insertion Sort](https://www.geeksforgeeks.org/insertion-sort/)
- [Khan Academy: Insertion Sort](https://www.khanacademy.org/computing/computer-science/algorithms/insertion-sort/a/insertion-sort)
