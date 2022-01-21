#%% Keyword - "in"
myInput = input("What day is today?")
if myInput in ["Sunday", "Saturday"]:
    print(myInput + " is a holiday in most of the countries")
else:
    print('You said, "' + myInput + '"')

#%% To check word in a string
"Hello" in "I just want to say Hello to you"
"Hello" in "I just want to say Hellos to you"

#%% Keyword - "pass"

def myFunc01():
    pass

myFunc01()

#%% Keyword - "is"
type(5) is int
type(5) is str
type("Hello") is str

#%% Keyword - "id" ( = object's memory address)
something = 5
print(id(something))

# %%
