# Bubble Sort Algorithm

## 📚 Introduction

![Example Image](https://www.simplilearn.com/ice9/free_resources_article_thumb/Bubble-Sort-Algorithm-Soni/working-of-bubble-sort-algorithm1png.png)

Bubble Sort is a straightforward and intuitive sorting algorithm that repeatedly compares adjacent elements in a list and swaps them if they are in the wrong order. It is often used for educational purposes to teach basic sorting concepts due to its simplicity.

## 🌟 Origins and History

Bubble Sort has its roots in early computer science education. It was introduced as a simple method to sort a list of elements, providing a clear and easy-to-understand example of sorting algorithms. Despite its inefficiency for large datasets, its ease of implementation makes it a valuable tool for learning the fundamentals of sorting.

## 📜 Pseudocode

Here is a high-level pseudocode for Bubble Sort:

procedure bubbleSort(A: array of items)
n = length(A)
for i from 0 to n-1 do
swapped = false
for j from 0 to n-i-2 do
if A[j] > A[j+1] then
swap A[j] and A[j+1]
swapped = true
if not swapped then
break


### Explanation:
1. **Initialize**: Start by iterating through the entire list.
2. **Compare and Swap**: Compare each pair of adjacent elements. Swap them if they are out of order.
3. **Optimization**: If no elements were swapped during a pass, the list is sorted, and the algorithm terminates early.

## 🧩 Example

Consider the following array that needs to be sorted in ascending order:

[5, 3, 8, 4, 2]


**Pass 1:**
- Compare 5 and 3 → Swap → [3, 5, 8, 4, 2]
- Compare 5 and 8 → No swap → [3, 5, 8, 4, 2]
- Compare 8 and 4 → Swap → [3, 5, 4, 8, 2]
- Compare 8 and 2 → Swap → [3, 5, 4, 2, 8]

**Pass 2:**
- Compare 3 and 5 → No swap → [3, 5, 4, 2, 8]
- Compare 5 and 4 → Swap → [3, 4, 5, 2, 8]
- Compare 5 and 2 → Swap → [3, 4, 2, 5, 8]

**Pass 3:**
- Compare 3 and 4 → No swap → [3, 4, 2, 5, 8]
- Compare 4 and 2 → Swap → [3, 2, 4, 5, 8]

**Pass 4:**
- Compare 3 and 2 → Swap → [2, 3, 4, 5, 8]

After these passes, the array is sorted.

## 📝 Expected Result

For the given example array `[5, 3, 8, 4, 2]`, the sorted array after applying Bubble Sort should be:

[2, 3, 4, 5, 8]


This demonstrates the algorithm's effectiveness in sorting the list in ascending order.


## 🤝 Acknowledgements

- This implementation is a basic example used for educational purposes to demonstrate sorting algorithm principles.

Happy sorting! 🚀
