"""Problem:
    Given an array of integers that are out of order, determine the bounds of the smallest 
    window that must be sorted in order for the entire array to be sorted. 
   Example, 
    given [ 3 , 7 , 5 , 6 , 9] , you should return ( 1 , 3 ) . 
"""

#This solution is O(nlogn) since the sorted function in python uses the Timsort algorithm

def locate_smallest_window(arr):
    inf_bound = 0
    sup_bound = 100000000000
    sorted_array = sorted(arr)

    for i in range(len(arr)):
        if arr[i] != sorted_array[i] and inf_bound == 0:
            inf_bound = i;
        elif arr[i] != sorted_array[i] :
            sup_bound = i

    return (inf_bound, sup_bound)

print(locate_smallest_window([3, 7, 5, 6, 9]))
