# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    
    # while len(arr) > 0....
    if end >= start:
        middle = (start + end)//2
        if arr[middle] == target:
            return middle
        elif target < arr[middle]:
            return binary_search(arr, target, start, end - 1)
        else:
            return binary_search(arr, target, start + 1, end)
    else:
        return -1

# def binary_search(arr, target):
#     first = 0
#     last = (len(arr) - 1)

#     found = False

#     while first <= last and not found:
#         #first using first digit division
#         middle = (first + last)//2

#         if arr[middle] == target:
#             return middle

#         elif target < arr[middle]:
#             last = middle -1
#         else:
#             first = middle + 1


#     return -1  # not found


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass



