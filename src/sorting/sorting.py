# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left_arr, right_arr): #make sure to loop through in order to get the smallest number
    elements = len(left_arr) + len(right_arr)
    current_val = 0 #current val is not the actual val of index number it's to help us keep track of changes
    merged_arr = [0] * elements

    i=j=k=0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            merged_arr[k] = left_arr[i]
            i += 1 
        else: 
            merged_arr[k] = right_arr[j]
            j += 1 
            
        k += 1
    
    while i < len(left_arr):
        merged_arr[k] = left_arr[i]
        # left_arr.pop(i)
        i += 1
        k += 1
    
    while j < len(right_arr):
        merged_arr[k] = right_arr[j]
        j += 1
        k += 1



    return merged_arr

# print("test merge", merge([2,3,4],[45,60]))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    start = 0
    end = len(arr)

    # Your code here
    if len(arr) > 1:
        middle = (start + end ) // 2
        left_arr = arr[:middle] # "start" is implied
        right_arr = arr[middle:]
      
        left = merge_sort(left_arr)
        right = merge_sort(right_arr)
        arr = merge(left,right)

    return arr


print("sort test",merge_sort([2,4,1,33,400,25]))
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here

# def merge_sort_in_place(arr, l, r):
#     # Your code here

