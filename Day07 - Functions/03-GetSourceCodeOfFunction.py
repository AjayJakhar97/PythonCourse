
# %% Find the source code of a function
import inspect


def myAbs(number):
    if number > 0:
        return number
    else:
        return -number


source_myAbs = inspect.getsource(myAbs)
print(source_myAbs)
# it seems to work only for objects defined in a file. Not for those defined in interpreter

# %% Find the source code of a built-in function
source_max = inspect.getsource(max)  # max is a built-in function
print(source_max)

# %%
