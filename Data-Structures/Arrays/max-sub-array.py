"""Problem:
    Given an array of numbers, :find the maximum sum of any contiguous subarray of the array.
   Example, 
    * given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137,
    since we would take elements 42, 14, -5, and 86.
    *  Given the array [ -5, -1, -8, -9], the maximum sum would be 0, since we would choose not to 
    take any elements.
"""

def max_sub_array(arr):
    max_sum = 0
    temp_sum = 0
    for i in range(len(arr)):
        temp_sum = 0
        for j in range(i, len(arr)):
            temp_sum+=arr[j]
            if(temp_sum > max_sum):
                max_sum = temp_sum
    return max_sum

print(max_sub_array([ -5, -1, -8, -9]))