#%%  Find whether 14 exists in the array or not

def CheckNumber(MyArray, MyNumber)
    for item in MyArray
        if item == MyNumber
            return True
        else
            continue
    return False
arr = [18,12,9,14,78,50]
result = CheckNumber(arr, 124)
print(result)
