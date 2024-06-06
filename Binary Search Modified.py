def partition(array, low, high):
    pivot = array[high]  # choose where the divide will be
    i = low - 1

    for j in range(low, high):  # go through all elements and compare with pivot
        # if element smaller than pivot is found, swap with greater element pointed by 1
        if array[j] <= pivot:
            i = i + 1
            # swaps element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    #swap pivotal element with greater element specified by i
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low < high:
        mid = (low + high) // 2
        if data[low] > target or data[high] < target:
            return -1
        elif data[mid] == target:
            return mid
        elif data[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


#main code to use quicksort and binary search
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array:")
print(data)

#sort the array using quicksort
size = len(data)
quickSort(data, 0, size - 1)

print(f"Sorted Array in Ascending Order: ")
print(data)

#prompt user to input targer number
target = int(input("Enter the number you want to serach for: "))

#perform binary search on the sorted array
result = binary_search(data, target)

if result != -1:
    print("Element is present at position", str(result + 1))
else:
    print("Element is not present in array")