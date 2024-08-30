# Radix Sort Algorithm

## Introduction

![Example Image](https://i.sstatic.net/nm9Xg.png)

Radix Sort is a non-comparative sorting algorithm that sorts numbers by processing individual digits. It uses the digits' place values to achieve sorting. Radix Sort processes numbers digit by digit, starting from the least significant digit (LSD) or the most significant digit (MSD), depending on the implementation. This method is particularly effective for sorting integers and can outperform comparison-based algorithms in certain cases.

## Origins and History

![Harold H. Seward](https://cache.legacy.net/legacy/images/cobrands/bostonglobe/photos/BG-2000629245-Harold_Seward.1_20120621.jpgx?w=600&h=315)

Radix Sort was first introduced by Harold H. Seward in 1954. Unlike comparison-based algorithms like Quick Sort or Merge Sort, Radix Sort leverages the numerical properties of the data to achieve linearithmic time complexity. It’s particularly useful in scenarios where the range of input data is known and manageable.

## Pseudocode

```plaintext
RadixSort(array)
    max_value = find_max(array)
    exp = 1
    while max_value / exp > 0
        CountingSort(array, exp)
        exp = exp * 10

CountingSort(array, exp)
    n = length(array)
    output = new array of size n
    count = new array of size 10

    // Initialize count array
    for i = 0 to 9
        count[i] = 0

    // Store count of occurrences
    for i = 0 to n - 1
        index = (array[i] / exp) % 10
        count[index] = count[index] + 1

    // Update count array to contain actual position of this digit in output[]
    for i = 1 to 9
        count[i] = count[i] + count[i - 1]

    // Build the output array
    for i = n - 1 to 0
        index = (array[i] / exp) % 10
        output[count[index] - 1] = array[i]
        count[index] = count[index] - 1

    // Copy the output array to array[], so that array[] contains sorted numbers
    for i = 0 to n - 1
        array[i] = output[i]
```
## Explanation

Radix Sort works by sorting the elements based on their individual digits, either starting from the least significant digit (LSD) or the most significant digit (MSD). It uses a stable sorting algorithm, like Counting Sort, to handle the sorting of individual digits. This process is repeated for each digit position until all digits are processed.

- **Step 1:** Determine the maximum number in the array to find out the number of digits in the largest number.
- **Step 2:** For each digit position (starting from LSD or MSD), perform a stable sort on the array based on that digit.
- **Step 3:** Repeat the sorting process for each digit position until all positions are covered.
- **Step 4:** The array is considered sorted when all digit positions have been processed.

## Example

Let's consider an example of sorting an array `[170, 45, 75, 90, 802, 24, 2, 66]` using Radix Sort:

1. **Digit Position:** Start with the least significant digit.
2. **Counting Sort:** Perform Counting Sort based on the current digit position.
3. **Move to Next Digit:** Move to the next significant digit and repeat the process.
4. **Combine Results:** Combine the results to produce the final sorted array.

### Detailed Steps:

1. **Sorting by Least Significant Digit (LSD):** Sort the array based on the units place.
2. **Sorting by Next Digit:** Move to the tens place and sort the array again.
3. **Sorting by Next Digit:** Move to the hundreds place and sort the array again.
4. **Final Sorted Array:** After sorting based on all digit positions, the array will be sorted.

## Expected Result

The sorted array after applying Radix Sort on `[170, 45, 75, 90, 802, 24, 2, 66]` will be:

`[2, 24, 45, 66, 75, 90, 170, 802]`

## Conclusion

Radix Sort is a highly efficient non-comparative sorting algorithm that can outperform comparison-based algorithms in certain scenarios. It is particularly effective when dealing with integers and when the range of the input data is known. By sorting digits from the least significant to the most significant, Radix Sort can achieve linear time complexity in practice, making it a valuable tool for large datasets.

Feel free to explore the code and contribute to its improvement. Happy coding!

## References

- [Wikipedia: Radix Sort](https://en.wikipedia.org/wiki/Radix_sort)
- [GeeksforGeeks: Radix Sort](https://www.geeksforgeeks.org/radix-sort/)
- [Khan Academy: Radix Sort](https://www.khanacademy.org/computing/computer-science/algorithms/radix-sort/a/overview-of-radix-sort)
