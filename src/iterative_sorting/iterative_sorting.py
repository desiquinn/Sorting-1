# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # for all indices EXCEPT the last index:
    for i in range(0, len(arr) - 1):
        # start with current index = 0
        cur_index = i
        # store the index of the smallest value in a temp variable
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # loop through elements on right-hand-side of current index
        for e in range(i+1, len(arr)):
            # find the smallest element by:
            # If an element is smaller than the value of the index currently stored in smallest_index
            if arr[e ] < arr[smallest_index]:
                #replace the currently stored index with that element's index
                smallest_index = e
        # TO-DO: swap
        # store element at cur_index in temp variable
        cur_value = arr[cur_index]
        # assign the cur_index in the list to the smallest_index's element
        arr[cur_index] = arr[smallest_index]
        # assign the smallest_index in the list to the original stored value
        arr[smallest_index] = cur_value
    return arr

    
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # count how many swaps are happening
    swap = True
    #Loop through the array while count is greater than 0
    while swap == True:
        swap_count = 0
        for i in range(len(arr)-1):
            # if el is greater that the next el:
            if arr[i] > arr[i+1]:
                # store the element in temp varriable
                cur_value = arr[i]
                # assign current index to value of next el
                arr[i] = arr[i+1]
                # assign next index to value of stored element
                arr[i+1] = cur_value
                # add 1 to counter
                swap_count += 1
        if swap_count == 0:
            swap = False

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr