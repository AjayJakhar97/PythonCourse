# %% Binary Search (Ordered - ASC and DESC)
# Find position (or index) of a number in a sorted list. 
# It can be increasing or decreasing order

def findIndex(arr, target):
    start = 0
    end = len(arr)-1
    isAscending = arr[start] < end

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
            return mid

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
    return -1
# program starts here...
# ============================

arr = [1, 2, 4, 5, 12, 15, 17, 20, 22, 44, 50]
# arr = [50, 44, 22, 20, 17, 15, 12, 5, 4, 2, 1]
target = 16
print(findIndex(arr, target))

#%% Find position (or index) of a number in a sorted list in an infinite list.

def search(arr, target,start,end):
    while start <= end:
        mid = int(start + (end - start) / 2)
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def findIndex(arr, target):
    start = 0
    end = 1
    while arr[end] < target:
        start = end + 1
        end = start + (end * 2)
    return search(arr, target, start, end)

arr = [1, 2, 4, 5, 12, 15, 17, 20, 22, 44, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
# arr = [50, 44, 22, 20, 17, 15, 12, 5, 4, 2, 1]
target = 4
print(findIndex(arr, target))

