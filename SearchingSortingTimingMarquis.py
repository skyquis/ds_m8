# Imports
import random
import time


# LINEAR SEARCH
# Linear Search method that will search list one element at a time to see if it matches "a"
def linear_search(numeric_list, a):
    for j in range(len(list)):
        if list[j] == a:
            return j
    # If match can't be found, return -1
    return -1


# BINARY SEARCH
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


if __name__ == '__main__':

    # First randomly generated array of 10000 values
    ten_k_array = [random.randint(0, 1000) for _ in range(10000)]

    print("\nRaw array is:")
    for j in range(len(ten_k_array)):
        print("% d" % ten_k_array[j], end=" ")

    start = time.process_time()
    bubblesort(ten_k_array)
    end = time.process_time()
    print("\nTime to bubble sort was " + str(end - start) + "seconds")

    print("\nSorted array is:")
    for k in range(len(ten_k_array)):
        print("% d" % ten_k_array[k], end=" ")

    # Second randomly generated array of 10000 values
    ten_k_array_second = [random.randint(0, 1000) for _ in range(10000)]

    print("\nRaw array is:")
    for j in range(len(ten_k_array_second)):
        print("% d" % ten_k_array_second[j], end=" ")

    start = time.process_time()
    selectionsort(ten_k_array_second)
    end = time.process_time()
    print("\nTime to selection sort was " + str(end - start) + "seconds")

    print("\nSorted array is:")
    for k in range(len(ten_k_array_second)):
        print("% d" % ten_k_array_second[k], end=" ")


##### INSERTION SORT

##### SUMMARY AND CONCLUSION