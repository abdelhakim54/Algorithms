"""Problem:
    Given an array of numbers, :find the maximum sum of any contiguous subarray of the array.
   Example, 
    * given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137,
    since we would take elements 42, 14, -5, and 86.
    *  Given the array [ -5, -1, -8, -9], the maximum sum would be 0, since we would choose not to 
    take any elements.
"""
# brute force solution
def max_sub_array(arr):#this algorithms time complexity is O(n²)
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


# solution using Kadane's Algorithm 
"""pseudo code:
    1- Define two-variable currSum which stores maximum sum ending here and maxSum which stores maximum sum so far.
    Initialize currSum with 0 and maxSum with INT_MIN.
    2- Now, iterate over the array and add the value of the current element to currSum and check
        * If currSum is greater than maxSum, update maxSum equals to currSum.
        * If currSum is less than zero, make currSum equal to zero.
    3- Finally, print the value of maxSum.
"""
def max_sub_array_sum(arr):
    curr_sum = 0
    max_sum = 0 # max sum so far
    for i in range(len(arr)):
        curr_sum += arr[i]
        if(curr_sum > max_sum):
            max_sum = curr_sum
        elif curr_sum < 0 :
            curr_sum = 0
    return max_sum

print(max_sub_array_sum([34, -50, 42, 14, -5, 86]))