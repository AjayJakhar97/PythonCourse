# %% Binary Search (Ordered - ASC and DESC)
# Find the index of number if you have an ordered list. It can be increasing or decreasing order

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

# %% Task - You need to guess if number is correct or not
# You have 3 chances
# Output should be 
    #  "That's the correct number" if guessed correctly or...
    # 'Sorry! You exhausted 3 chances' if missed all chances

import random

def GuessTheNumber():
    chances = 3
    luckyNumber = random.randint(1,10)
    while(chances > 0):
        myNumber = int(input("Enter a number from 1 to 10: "))
        if myNumber == luckyNumber:
            return "That's the correct number"
        chances -= 1
    else:
        return "Sorry! You exhausted 3 chances"

GuessTheNumber()


# %%

chances = 3
while(chances > 0):
    myNumber = int(input("Enter the number: "))
    if myNumber == 3:
        print("That's the correct number")
    chances -= 1
elif chances == 0:
    print("Sorry! You exhausted 3 chances")
