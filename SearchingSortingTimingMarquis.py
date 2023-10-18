# Imports
import random
import time


# LINEAR SEARCH
# Linear Search method that will search list one element at a time to see if it matches "a"
def linear_search(numeric_list, a):
    for j in range(len(numeric_list)):
        if numeric_list[j] == a:
            return j
    # If match can't be found, return -1
    return -1


# BINARY SEARCH
# Binary search which will requires sorted data. It will look at midpoint and throw away half the data at a time until,
# it finds data it is looking for, or runs out of data
def binary_search(numeric_list, b):
    low = 0
    high = len(numeric_list) - 1
    while low <= high:
        # Find middle using low and high
        middle = (low + high) // 2
        # If b is greater than value at middle index, ignore left side including the middle index
        if b > numeric_list[middle]:
            low = middle + 1
        # if b is less than value at middle index, ignore right side including the middle index
        if b < numeric_list[middle]:
            high = middle - 1
        else:
            return middle
    return -1


# BUBBLE SORT
# Python program for implementation of Bubble Sort. Obtained from
# "https://www.geeksforgeeks.org/python-program-for-bubble-sort/"
def bubblesort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return


# SELECTION SORT
# Selection sort in Python
# Obtained and adapted from https://www.geeksforgeeks.org/python-program-for-selection-sort/
# time complexity O(n*n)
# sorting by finding min_index
def selectionsort(array):
    for ind in range(len(array)):
        min_index = ind

        for j in range(ind + 1, len(array)):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])


# INSERTION SORT
# Obtained from https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertionsort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position


if __name__ == '__main__':

    # Bubble sort execution
    # First randomly generated array of 10000 values
    ten_k_array = [random.randint(0, 1000) for _ in range(10000)]

    # Perform linear search for constant value "500"
    VALUE = 500
    ls_index = linear_search(ten_k_array, VALUE)
    if ls_index == -1:
        print("\nValue 500 not found in array")
    else:
        print("\nValue 500 found in index " + str(ls_index))

    """print("\nRaw array is:")
    for j in range(len(ten_k_array)):
        print("% d" % ten_k_array[j], end=" ")"""

    start = time.process_time()
    bubblesort(ten_k_array)
    end = time.process_time()
    print("\nTime to bubble sort was " + str(end - start) + " seconds")

    """print("\nSorted array is:")
    for k in range(len(ten_k_array)):
        print("% d" % ten_k_array[k], end=" ")"""

    # Randomly generated array of x values - to approximate 30 seconds
    thirty_sec_array = [random.randint(0, 1000) for _ in range(31000)]

    """print("\nRaw array is below. Size of array is " + str(len(thirty_sec_array)))
    for j in range(len(thirty_sec_array)):
        print("% d" % thirty_sec_array[j], end=" ")"""

    start = time.process_time()
    bubblesort(thirty_sec_array)
    end = time.process_time()
    print("\nTime to bubble sort was " + str(end - start) + " seconds")

    """print("\nSorted array is:")
    for k in range(len(thirty_sec_array)):
        print("% d" % thirty_sec_array[k], end=" ")"""

    # Perform binary search for constant value 500
    bs_index = binary_search(ten_k_array, VALUE)
    if bs_index == -1:
        print("\nValue 500 not found in array")
    else:
        print("\nValue 500 found in index " + str(bs_index))

    # Second randomly generated array of 10000 values
    ten_k_array_second = [random.randint(0, 1000) for _ in range(10000)]

    # Perform linear search for constant value "500"
    VALUE = 500
    ls_index = linear_search(ten_k_array_second, VALUE)
    if ls_index == -1:
        print("\nValue 500 not found in array")
    else:
        print("\nValue 500 found in index " + str(ls_index))

    """print("\nRaw array is:")
    for j in range(len(ten_k_array_second)):
        print("% d" % ten_k_array_second[j], end=" ")"""

    start = time.process_time()
    selectionsort(ten_k_array_second)
    end = time.process_time()
    print("\nTime to selection sort was " + str(end - start) + " seconds")

    """print("\nSorted array is:")
    for k in range(len(ten_k_array_second)):
        print("% d" % ten_k_array_second[k], end=" ")"""

    # Randomly generated array of x values - to approximate 30 seconds
    thirty_sec_array_second = [random.randint(0, 1000) for _ in range(30000)]

    """print("\nRaw array is below. Size of array is " + str(len(thirty_sec_array_second)))
    for j in range(len(thirty_sec_array_second)):
        print("% d" % thirty_sec_array_second[j], end=" ")"""

    start = time.process_time()
    bubblesort(thirty_sec_array_second)
    end = time.process_time()
    print("\nTime to selection sort was " + str(end - start) + " seconds")

    """print("\nSorted array is:")
    for k in range(len(thirty_sec_array_second)):
        print("% d" % thirty_sec_array_second[k], end=" ")"""

    # Perform binary search for constant value 500
    bs_index = binary_search(ten_k_array_second, VALUE)
    if bs_index == -1:
        print("\nValue 500 not found in array")
    else:
        print("\nValue 500 found in index " + str(bs_index))

    # Third randomly generated array of 10000 values
    ten_k_array_third = [random.randint(0, 1000) for _ in range(10000)]

    # Perform linear search for constant value "500"
    VALUE = 500
    ls_index = linear_search(ten_k_array_third, VALUE)
    if ls_index == -1:
        print("\nValue 500 not found in array")
    else:
        print("\nValue 500 found in index " + str(ls_index))

    """print("\nRaw array is:")
    for j in range(len(ten_k_array_third)):
        print("% d" % ten_k_array_third[j], end=" ")"""

    start = time.process_time()
    insertionsort(ten_k_array_third)
    end = time.process_time()
    print("\nTime to insertion sort was " + str(end - start) + " seconds")

    """print("\nSorted array is:")
    for k in range(len(ten_k_array_third)):
        print("% d" % ten_k_array_third[k], end=" ")"""

    # Randomly generated array of x values - to approximate 30 seconds
    thirty_sec_array_third = [random.randint(0, 1000) for _ in range(32000)]

    """print("\nRaw array is below. Size of array is " + str(len(thirty_sec_array_second)))
    for j in range(len(thirty_sec_array_second)):
        print("% d" % thirty_sec_array_second[j], end=" ")"""

    start = time.process_time()
    bubblesort(thirty_sec_array_third)
    end = time.process_time()
    print("\nTime to insertion sort was " + str(end - start) + " seconds")

    """print("\nSorted array is:")
    for k in range(len(thirty_sec_array_second)):
        print("% d" % thirty_sec_array_second[k], end=" ")"""

    # Perform binary search for constant value 500
    bs_index = binary_search(ten_k_array_third, VALUE)
    if bs_index == -1:
        print("\nValue 500 not found in array")
    else:
        print("\nValue 500 found in index " + str(bs_index))

##### INSERTION SORT

##### SUMMARY AND CONCLUSION