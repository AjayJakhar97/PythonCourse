# %% Given a characters array letters that is sorted in ascending order and a character target, return the smallest character in the array that is larger than target
# Note: characters warp around

def findCeiling(arr, target):
    start = 0
    end = len(arr) - 1

    isAscending = arr[start] < arr[end]
    
    while start <= end:
        mid = int(start + (end - start) / 2)

        if isAscending:
            if target < arr[mid]:
                end = mid -1
            else:
                start = mid + 1
        else:
            if target > arr[mid]:
                end = mid -1
            else:
                start = mid + 1
    return arr[start % len(arr)]

arr = ['c', 'e', 'x', 'z']
target = 'z'

result = findCeiling(arr, target)
print(result)
