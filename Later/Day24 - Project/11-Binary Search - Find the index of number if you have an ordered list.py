# %% Binary Search (Ordered - ASC and DESC)
# Find the index of number if you have an ordered list. It can be increasing or decreasing order

# arr = [1, 2, 4, 5, 12, 15, 17, 20, 22, 44, 50]
arr = [50, 44, 22, 20, 17, 15, 12, 5, 4, 2, 1]

target = 155

start = 0
end = len(arr)-1

while start <= end:

    mid = int(start + (end - start) / 2)

    '''
    mid = (start + end) / 2
    => (start + start - start + end) / 2
    => (2start + end - start) / 2
    => (2start)/2 + (end - start) / 2
    => start + (end - start) / 2
    '''

    if arr[0] < arr[len(arr)-1]:
        isAscending = True
    else:
        isAscending = False


    if arr[mid] == target:
        print(mid)
        break
    else:
        if isAscending:
            if arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if arr[mid] > target:
                start = mid + 1
            else:
                end = mid - 1
else:
    print("Element doesn't exist")
# %%
