# def linear_search(arr, target):
#     # Your code here


#     return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:  
        middle = low + high // 2    
        checkpoint = arr[middle]
        if checkpoint == target:
            return middle
        if target < checkpoint:
            low = middle - 1
        if target > checkpoint:
            high = middle + 1
        return -1


    return -1
