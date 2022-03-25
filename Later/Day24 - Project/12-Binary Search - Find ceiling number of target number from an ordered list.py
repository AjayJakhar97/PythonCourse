# %% Binary Search (Ordered - ASC and DESC)
# Find the index of number if you have an ordered list. It can be increasing or decreasing order

arr = [1, 2, 4, 5, 12, 15, 17, 20, 22, 44, 50]
# arr = [50, 44, 22, 20, 17, 15, 12, 5, 4, 2, 1]

target = 17

start = 0
end = len(arr)-1
isAscending = arr[start] < end

while start <= end:
    mid = int(start + (end - start) / 2)
    '''
    Below is the explaination
    ========================
    mid = (start + end) / 2
    => (start + start - start + end) / 2
    => (2start + end - start) / 2
    => (2start)/2 + (end - start) / 2
    => start + (end - start) / 2
    '''
    if arr[mid] == target:
        print(mid)

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
else:
    print("Element doesn't exist")
# %%
