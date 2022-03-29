#%%  16-find first and last element of target element in a sorted array
'''

'''
def myFunction(arr,target):
    first = 0
    last = 0
    for item in range(len(arr)):
        if arr[item] == target and first == 0:
            first = item
        else:
            first = item

arr = [5,7,7,7,7,8,8,10]
target = 7
result = myFunction(arr,target)
print(result)

