# %% Linear Search (Ordered - ASC and DESC)
# Find the index of number if you have an ordered list. It can be increasing or decreasing order

# arr = [1, 2, 4, 5, 12, 15, 17, 20, 22, 44, 50]

arr = [50, 44, 22, 20, 17, 15, 12, 5, 4, 2, 1]

target = 50

for item in arr:
    if target == item:
        print(arr.index(item))
        break
    else:
        continue
else:
    print("Element doesn't exist")

# %%
