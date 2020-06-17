# TO-DO: complete the helper function below to merge 2 sorted arrays
# MergeSort(arr[], l,  r)
# If r > l
#      1. Find the middle point to divide the array into two halves:  
#              middle m = (l+r)/2
#      2. Call mergeSort for first half:   
#              Call mergeSort(arr, l, m)
#      3. Call mergeSort for second half:
#              Call mergeSort(arr, m+1, r)
#      4. Merge the two halves sorted in step 2 and 3:
#              Call merge(arr, l, m, r)
def merge(arrA, arrB):
    merged_arr = []

    #until one of the arrays has no elements left, add the frontmost element as long as it's smaller
    while (len(arrA) + len(arrB)) > 0:
        #if one of the arrays is empty, just append the rest of the other one to the new array
        if len(arrA) == 0:
            merged_arr.append(arrB.pop(0))
        elif len(arrB) == 0:
            merged_arr.append(arrA.pop(0))
        elif arrA[0] < arrB[0]:
            merged_arr.append(arrA.pop(0)) 
        else:
            merged_arr.append(arrB.pop(0))
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
# 16
# 8 8
# 4 4 4 4
# 2 2 2 2 2 2 2 2 
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 2 2 2 2 2 2 2 2 
# 4 4 4 4
# 8 8
# 16
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr)//2
        arr1 = merge_sort(arr[:middle])
        arr2 = merge_sort(arr[middle:])
        return merge(arr1,arr2)
       
    
    
    # return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

