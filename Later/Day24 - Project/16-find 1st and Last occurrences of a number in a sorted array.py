#%%  find first and last occurrences element of target element in a sorted array

def search(arr,target,findStartIndex):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = start + (end-start)//2
        if arr[mid] == target:
            ans = mid
            if findStartIndex:
                end = mid - 1
            else:
                start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return ans

arr = [5,7,7,7,7,8,8,10]
target = 7
ans = [-1,-1]
ans[0] = search(arr,target,True)
if ans[0] != -1:
    ans[1] = search(arr,target,False)
print(ans)

# %%
