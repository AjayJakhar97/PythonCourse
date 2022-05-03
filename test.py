#%% How can run a function to run when you want without blocking others?

import nest_asyncio
nest_asyncio.apply()

#%% Let's analyze the problem we may encounter with a normal function 

def searcher1(myTxt):
    book = 'This is a good book'
    while True:
        txt = myTxt
        if txt in book:
            print(f'{txt} - exists')
        else:
            print(f'{txt} - doesn\'t exist')
#%% You will notice you can't send argument and the next line never gets a chance to execute either
searcher1('good')
print('Hey')

#%% Let's try to use generator instead with yield to use whenever we want to use it

def searcher2():
    book = 'This is a good book'
    while True:
        txt = yield
        if txt in book:
            print('Yes')
        else:
            print('No')

myVar = searcher2()


#%%
# next(myVar)
myVar.send(None)
myVar.send('book')
print('Hey')
myVar.send('books')

#%%
print(type(searcher1))
print(type(myVar))


# %% Let's look at a routine (or functions, subroutine, methods, procedures )
# Routine is a set of instructions executed in a sequence to perform a specific task
# but routine ( or functions) are non-cooperative
# The problem with routine is that it won't pass control until finished executing. 

import time
def routineOne():
    print('Routine One started...')
    time.sleep(3)
    print('Routine One stopped...')

def routineTwo():
    print('Routine Two started...')
    time.sleep(3)
    print('Routine Two stopped...')

routineOne()
routineTwo()

# %% A normal function is also a routine and we can verify with below code
import inspect
inspect.isroutine(routineOne)

#%%
'''
Execution of Python coroutines can be suspended and resumed at many points. 

1- await expressions, 
2- async for and 
3- async with 

can only be used in the body of a coroutine function.

Functions defined with async def syntax are always coroutine functions, even if they do not contain await or async keywords.

It is a SyntaxError to use a yield from expression inside the body of a coroutine function

'''
#%% Now let's convert this non-cooperative routines to cooperative routines a.k.a coroutine

import time
async def coRoutineOne():
    print('CoRoutine One started...')
    time.sleep(3)
    await coRoutineTwo()
    print('CoRoutine One stopped...')

async def coRoutineTwo():
    print('CoRoutine Two started...')
    time.sleep(3)
    print('CoRoutine Two stopped...')

asyncio.run(coRoutineOne())
asyncio.run(coRoutineTwo())

#%%
import inspect
inspect.iscoroutine(coRoutineOne)

# %%
'''
if you get "RuntimeWarning: coroutine 'coRoutineOne' was never awaited coRoutineOne()"

You made coRoutineOne an awaitable function, a coroutine, by using async def.

When you call an awaitable function, you create a new coroutine object. The code inside the function won't run until you then await on the function or run it as a task:

'''