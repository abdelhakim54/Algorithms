"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def brute_force_check_sum(arr, k):
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == k:
                return True
    return False

def two_pass_check_sum(arr, k):
    numMap = {}
    n = len(arr)

    for i in range(n):
        numMap[arr[i]] = i
    
    for i in range(n):
        compelement = k - arr[i]
        if compelement in numMap and numMap[compelement] != i:
            return True # [i, numMap[complement]]
    return False

def one_pass_check_sum(arr, k):
    numMap = {}
    n = len(arr)
    for i in range(n):
        compelement = k - arr[i]
        if compelement in numMap:
            return True
        numMap[arr[i]] = i
    return False


# if __name__=="__main__":
#     arr = [10, 15, 3, 7]
#     k = 17
#     brute_force_check_sum(arr, k)