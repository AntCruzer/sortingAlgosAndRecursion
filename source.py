# REFERENCES
from utils import *
import random





print("\nQUICK SORT (PIVOT AT LAST ELEMENT)")

arr = list(range(1, 11))                        # create array of random numbers

random.shuffle(arr)                             # randomize order

print("Unsorted array: {}".format(arr))

sorted_arr = quickSort(arr)

print("Sorted array: {}".format(sorted_arr))





print("\nBUBBLE SORT")

arr1 = list(range(1, 11))                       # create array of random numbers

random.shuffle(arr1)                            # randomize order

print("Unsorted array: {}".format(arr1))

sorted_arr1 = bubbleSort(arr1)

print("Sorted array: {}".format(sorted_arr1))





print("\nMERGE SORT")

arr2 = list(range(1, 11))                       # create array of random numbers

random.shuffle(arr2)                            # randomize order

print("Unsorted array: {}".format(arr2))

sorted_arr2 = mergeSort(arr2)

print("Sorted array: {}".format(sorted_arr2))





print("\nINSERTION SORT")

arr3 = list(range(1, 11))                       # create array of random numbers

random.shuffle(arr3)                            # randomize order

print("Unsorted array: {}".format(arr3))

sorted_arr3 = insertionSort(arr3)

print("Sorted array: {}".format(sorted_arr3))





print("\nEND OF PROGRAM\n")