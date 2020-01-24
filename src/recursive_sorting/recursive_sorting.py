# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # print(f"arrA: {arrA}")
    # print(f"arrB: {arrB}")
    # print(f"merged array: {merged_arr}")
    # TO-DO
    a = 0 # Counting index of arrA
    b = 0 # Counting index of arrB
    # loop through merged_arr
    for i in range(len(merged_arr)):
        # compare arrA[0] to arrB[0] to find smallest and add to current index of merged_arr
        if a >= len(arrA): # Then there is nothing left to check in arrA
            merged_arr[i] = arrB[b] # So add the rest of arrB
            b += 1 # Increase index of arrB counter
            # print (merged_arr)
        elif b >= len(arrB): # Then there is nothing left to check in arrB
            merged_arr[i] = arrA[a] # So add the rest of arrA
            a += 1 # Increase index of arrA counter
            # print (merged_arr)
        elif arrA[a] < arrB[b]:
            # add the value of smallest to current index
            merged_arr[i] = arrA[a]
            a += 1
            # print (merged_arr)
        else:
            merged_arr[i] = arrB[b]
            b += 1
            # print (merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # print(f"array in merge_sort: {arr}")
    # TO-DO
    mid = len(arr) // 2
    #coverge on base case: split the array into two halves
    if len(arr) > 1:
        # send array back into merge_sort to be split again
        half1 = merge_sort(arr[:mid])
        half2 = merge_sort(arr[mid:])
        # if the length of both halves is 1 then send each into Merge
        # print(f"Send: {half1}, {half2}")
        return merge(half1, half2)
    return arr

# merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])





# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
