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
# %%
