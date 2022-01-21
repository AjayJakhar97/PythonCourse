#%% Create a quick list
fruits = ["apple", "banana", "cherry"]

#%% Let's get each item from the list
for items in fruits:
    print(items)

#%% Let's get output on single line with seperator like space ' ' or a comma , etc.
for items in fruits:
    print(items, end=' ')

for items in fruits:
    print(items, end=',')

#%% We can also output positions along with elements like below
for items in range(len(fruits)):
    print(items, " - ", fruits[items])
# %%
