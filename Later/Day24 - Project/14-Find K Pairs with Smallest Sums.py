# %% Find K Pairs with Smallest Sums

'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k. Define a pair (u,v) which consists of one element from the first array and one element from the second array.
Find the k pairs (u1,v1),(u2,v2) …(uk,vk) with the smallest sums.
Return results need to be orderly.

Example 1
===============
nums1 = [1,7,11]
nums2 = [2,4,6]

k = 3

Return: [1,2],[1,4],[1,6]

Example 2
===============
nums1 = [1,7,11]
nums2 = [2,4,6]

k = 4

Return: [1,2],[1,4],[1,6][7,2]

'''

def MyFunc_GetIndex_SmallestSum(num1, num2, k):
    counter = 1
    result = []

    for i in range(len(num1)):
        for j in range(len(num2)):
            if counter <= k:
                result.append([i, j])
                counter += 1
    return result

def MyFunc_GetNumbers_SmallestSum(num1, num2, k):
    counter = 1
    result = []

    for i in num1:
        for j in num2:
            if counter <= k:
                result.append([i, j])
                counter += 1
    return result

num1 = [1, 7, 11]
num2 = [2, 4, 6]
k = 2

result = MyFunc_GetIndex_SmallestSum(num1, num2, k)
print(result)

result = MyFunc_GetNumbers_SmallestSum(num1, num2, k)
print(result)

#%% 

