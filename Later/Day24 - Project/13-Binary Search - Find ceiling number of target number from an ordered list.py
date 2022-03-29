# %% Binary Search (Ordered - ASC and DESC)
# Find the ceiling of number if you have an ordered list. It can be increasing or decreasing order

def findCeiling(arr, target):
    start = 0
    end = len(arr)-1
    isAscending = arr[start] < end

    if isAscending:
        if target > arr[len(arr)-1]:
            return "no ceiling for this number"
    else:
        if target < arr[len(arr)-1]:
            return "no ceiling for this number"
    while start <= end:
        mid = int(start + (end - start) / 2)
    
        '''
    Below is the explanation
    ========================
    mid = (start + end) / 2
    => (start + start - start + end) / 2
    => (2start + end - start) / 2
    => (2start)/2 + (end - start) / 2
    => start + (end - start) / 2
    '''
        if arr[mid] == target:
            if mid == len(arr)-1:
                return "No ceiling for this number"
            else:
                return arr[mid+1]

        if isAscending:
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target > arr[mid] :
                end = mid - 1
            else:
                start = mid + 1
    return arr[mid]

# program starts here...
# ============================

arr = [1, 2, 4, 5, 12, 15, 17, 20, 22, 44, 50]
# arr = [50, 44, 22, 20, 17, 15, 12, 5, 4, 2, 1]
target = 49
print(findCeiling(arr, target))

# %%
