#%% Below code shows tuple are immutable as the ID means object is changed if we change it
list_data = ['an', 'example', 'of', 'a', 'list']
tuple_data = ('this', 'is', 'an', 'example', 'of', 'tuple')

# get IDs of them
print(id(list_data))
print(id(tuple_data))

# Adding elements to list and tuple
list_data += ['Headset']
tuple_data += ('Keyboard','mouse')

# print them
print(list_data)
print(tuple_data)

# get IDs of them
print(id(list_data))
print(id(tuple_data))

#%% You can't compare list with tuple
list_data = [1,2,33,5,2]
tuple_data = (1,2,33,5,2)
print(list_data != tuple_data)

# %% You can create a list of tuple by putting () around a the elements
studentList = ("Ram", "Gita", "Chris")
print(studentList)

count = 0
for item in studentList:
    count = count + 1
print(f"Total elements : {count}")

#%% even this will create a tuple 
studentList = "Ram", "Gita", "Chris"

print(studentList)

count = 0
for item in studentList:
    count = count + 1
print(f"Total elements : {count}")

#%% but we shouldn't do this. try 

studentList1 = "Ram"
print(studentList1)
count = 0
for item in studentList1:
    count = count + 1
print(f"Total elements : {count}")

#%%
studentList2 = ("Ram")
print(studentList2)

count = 0
for item in studentList2:
    count = count + 1
print(f"Total elements : {count}")

#%% What if have to get one element out of this for example just "Ram" as one?
studentList = ["Ram"]

count = 0
for item in studentList:
    count = count + 1
print(count)