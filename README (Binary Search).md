# YR-11-T2-2024

# Binary Search and Quicksort Algorithms

## Description
This Python module provides implementations of the binary search and quicksort algorithms, two fundamental techniques in computer science for searching and sorting data efficiently.

## Features
`Quicksort`: A sorting algorithm that employs a divide-and-conquer strategy to sort an array in ascending order.
`Binary Search`: A searching algorithm for finding the position of a target value within a sorted array.
`Modular Design`: Both algorithms are implemented as separate functions, allowing for easy integration into other projects.

# Example usage of quickSort
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
quickSort(array, 0, len(array) - 1)

# Example usage of binary_search
index = binary_search(array, 4)
if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")

# Functions
- `quickSort(array, low, high)`: Sorts the elements of the array in ascending order using the quicksort algorithm.
- `binary_search(data, target)`: Searches for the target value within the sorted data array and returns its index if found, otherwise returns -1.
