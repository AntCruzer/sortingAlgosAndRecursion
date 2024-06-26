"""
    FUNCTION            :       quickSort()
    PARAMETERS          :       array
    RETURNS             :       orderedArray
    DESCRIPTION         :       This function organizes an array via 
                                quick sort recursively and returns the 
                                ordered array.
    BIG-O (WORST CASE)  :       O(n^2) 
"""
def quickSort(array):

    # BASE CASE
    if len(array) <= 1:
        return array
    
    # CHECK IF ARRAY ALREADY SORTED
    if array == sorted(array):
        return array

    else:
        # SET PIVOT AT END OF ARRAY
        pivot = array[-1]                                          

        # IDENTIFY PARTITIONS
        first_partition = [x for x in array[:-1] if x <= pivot]
        second_partition = [x for x in array[:-1] if x > pivot]

        # RECURSIVELY CALL QUICKSORT FOR EACH PARTITION
        return quickSort(first_partition) + [pivot] + quickSort(second_partition)
    




"""
    FUNCTION            :       bubbleSort()
    PARAMETERS          :       array
    RETURNS             :       array
    DESCRIPTION         :       This function organizes an array via 
                                bubble sort recursively and returns the 
                                ordered array.
    BIG-O (WORST CASE)  :       O(n^2) 
"""
def bubbleSort(array):

    # ARRAY LENGTH
    n = len(array)

    # BASE CASE
    if n <= 1:
        return array
    
    # CHECK IF ARRAY ALREADY SORTED
    if array == sorted(array):
        return array

    else:
       # outer loop has final say to determine to if list is fuly sorted
       # each time outer loop passes, greatest value is at the end
       for i in range(n):
           
           # inner loop performs adjacent element comparisons and swapping
           for j in range(0, n-i-1):
               
               # range decreaeses over time as elements are organinzed for least to greatest
               if array[j] > array[j+1]:
                   
                   # swap values
                   array[j], array[j+1] = array[j+1], array[j]

    return array





"""
    FUNCTION            :       mergeSort()
    PARAMETERS          :       array
    RETURNS             :       array
    DESCRIPTION         :       This function organizes an array via 
                                merge sort recursively and returns the 
                                ordered array.
    BIG-O (WORST CASE)  :       O(n log n) 
"""
def mergeSort(arr):

    # BASE CASE
    if len(arr) <= 1:
        return arr
    
    # MIDDLE OF ARRAY
    mid = len(arr) // 2
    
    # IDENTIFY HALVES
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # RECURSIVELY CALL SPLITTER FUNCTION UNITL BASE CASE REACHED
    left_sorted = mergeSort(left_half)
    right_sorted = mergeSort(right_half)
    
    # FOR EVERY TIME ARRAY WAS SPLIT, ARRANGE ELEMENTS IN ORDER
    return merge(left_sorted, right_sorted)





"""
    FUNCTION            :       merge()
    PARAMETERS          :       left, right
    RETURNS             :       sorted_array
    DESCRIPTION         :       This function performs the merging of both array
                                elements into a singular array.
"""
def merge(left, right):

    sorted_array = []
    i = j = 0               # SET COUNTER
    
    # LOOP HAPPENS AS LONG THERE ARE ELEMENTS TO COMPARE IN BOTH ARRAYS
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    # APPEND LEFT OVER ELEMENTS IN LEFT ARRAY
    while i < len(left):
        sorted_array.append(left[i])
        i += 1
    
    # APPEND LEFT OVER ELEMENTS IN RIGHT ARRAY
    while j < len(right):
        sorted_array.append(right[j])
        j += 1
    
    return sorted_array





"""
    FUNCTION            :       insertionSort()
    PARAMETERS          :       array
    RETURNS             :       array
    DESCRIPTION         :       This function organizes an array via 
                                insertion sort and returns the 
                                ordered array.
    BIG-O (WORST CASE)  :       O(n^2) 
"""
def insertionSort(array):

    # traverse through 1 to len(arr)
    for i in range(1, len(array)):
        
        cmp = array[i]      # value to be compared with ones before it
        j = i - 1           # j set before postion i

        # while j is in range AND cmp is less than element j
        while j >= 0 and cmp < array[j]:
            
            array[j + 1] = array[j]     # shift position of current j by 1 to the right
            j -= 1                      # decrement j position                   
        array[j + 1] = cmp              # increment cmp variable
    
    return array