# Heap Sort Algorithm

## Introduction

Heap Sort is an efficient comparison-based sorting algorithm that utilizes a binary heap data structure to sort elements. It is similar to the selection sort where we first find the maximum element and place it at the end of the array. The process is repeated for the remaining elements. Due to its O(n log n) time complexity in all cases (worst, average, and best), Heap Sort is particularly well-suited for large datasets. It is also an in-place sorting algorithm, meaning it does not require additional space for sorting.

Heap Sort builds a binary heap from the input data and then repeatedly extracts the maximum (or minimum, depending on the heap type) element from the heap and reconstructs the heap until all elements are sorted.

## Origins and History

![J. W. J. Williams](https://cdn-otf-cas.prfct.cc/dfs1/eyJ3IjozMDAsImQiOjcyLCJtIjoiSlBHIiwidXJsIjoiaHR0cHM6XC9cL2FkYXMtb3JlZ29uLWNhcy1vYml0cy5zMy5hbWF6b25hd3MuY29tXC9waG90b3NcL2NyZWF0ZV9zdG9yeVwvNWIzYzIzNWYwNGVkNVwvYTc0NDU3YjM0ZTczNzQyOWFiOWNhNzk2YTkyNS5qcGcifQ==)

Heap Sort was introduced by J. W. J. Williams in 1964 as a way to improve the selection sort's runtime efficiency. The algorithm utilizes a binary heap data structure, a concept central to efficient priority queue operations. Since its introduction, Heap Sort has been widely adopted for various applications, particularly where memory usage is a concern due to its in-place sorting capabilities.

## Pseudocode

```plaintext
HeapSort(array)
    BuildMaxHeap(array)
    for i = array.length - 1 to 1
        swap(array[0], array[i])
        heapSize = heapSize - 1
        MaxHeapify(array, 0)

BuildMaxHeap(array)
    heapSize = array.length
    for i = floor(array.length / 2) - 1 downto 0
        MaxHeapify(array, i)

MaxHeapify(array, i)
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < heapSize and array[left] > array[largest]
        largest = left

    if right < heapSize and array[right] > array[largest]
        largest = right

    if largest != i
        swap(array[i], array[largest])
        MaxHeapify(array, largest)
```

## Explanation

Heap Sort works by visualizing the elements of the array as a special kind of complete binary tree called a binary heap. The algorithm performs two main steps:

1. **Building a Max Heap:** First, it transforms the input array into a Max Heap. A Max Heap is a complete binary tree where the value of each node is greater than or equal to the values of its children.

2. **Extracting Elements from the Heap:** Repeatedly swap the root of the heap (the maximum element) with the last element in the array and then reduce the heap size by one. This effectively removes the maximum element from the heap, placing it in its correct sorted position. The heap is then restructured using a procedure called `MaxHeapify` to maintain the heap property.

## Example

Let's sort an array `[4, 10, 3, 5, 1]` using Heap Sort:

1. **Initial Array:** `[4, 10, 3, 5, 1]`

2. **Build Max Heap:**
   - Transform the array into a max heap: `[10, 5, 3, 4, 1]`

3. **Extract Maximum and Heapify:**
   - Swap the first element `10` with the last element `1` and reduce the heap size by 1. The array now looks like `[1, 5, 3, 4, 10]`.
   - Apply `MaxHeapify` to restore the heap property, resulting in `[5, 4, 3, 1, 10]`.

4. **Repeat the process:**
   - Swap the root `5` with the last element of the heap `1`, resulting in `[1, 4, 3, 5, 10]`.
   - Apply `MaxHeapify` to the reduced heap `[1, 4, 3]`, resulting in `[4, 1, 3, 5, 10]`.

5. **Continue until the heap is empty:**
   - Swap `4` with `3`, resulting in `[3, 1, 4, 5, 10]`.
   - Heapify `[3, 1]` to get `[3, 1, 4, 5, 10]`.
   - Swap `3` with `1`, resulting in `[1, 3, 4, 5, 10]`.

6. **Final Sorted Array:** `[1, 3, 4, 5, 10]`

The array is now sorted in ascending order.
