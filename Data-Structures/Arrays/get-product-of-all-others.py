
"""Problem:
    Given an array of integers, return a new array such that each element at index i of 
    the new array is the product of all the numbers in the original array except the one  at i
   Example:
     if our input was [ 1, 2, 3, 4, 5], the expected output would be [ 120, 60, 40, 30, 24].
     If our input was [3, 2, 1],the expected output would be [2,  3, 6]. 
"""

def getProduct(arr):
    newArr = []
    product = 1
    for i in range(len(arr)):
        product *= arr[i]
    for i in range(len(arr)):
        newArr.append(int(product / arr[i]))
    return newArr


print(getProduct([1, 2, 3, 4, 5]))

"follow-up: solution without division"

def getProd(arr):
    n = len(arr)
    prefix = []
    suffix = []
    myNewArr = []
    for i in range(n):
        if (prefix and suffix):
            prefix.append(prefix[-1]* arr[i])
            suffix.append(suffix[-1]* arr[n-i-1])
        else:
            prefix.append(arr[i])
            suffix.append(arr[n-1])
    suffix = suffix[::-1]

    for i in range(n):
        if i == 0:
            myNewArr.append(suffix[1])
        elif i == n-1:
            myNewArr.append(prefix[n-2])
        else :
            myNewArr.append(prefix[i-1] * suffix[i+1])
    return myNewArr

print(getProd([1, 2, 3, 4, 5]))