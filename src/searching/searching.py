def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found

# from decimal import Decimal, ROUND_HALF_UP
import math
# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (high+low)//2
        # print('middle', middle)
        if target == arr[middle]:
            # print('target is middle', middle)
            return middle

        elif arr[middle] > target:
            # print('target is less', middle)
            high = middle-1

        elif arr[middle] < target:
            # print('target is greater', middle)
            low = middle+1
        
    return -1  # not found

# arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

# binary_search(arr1, -8)