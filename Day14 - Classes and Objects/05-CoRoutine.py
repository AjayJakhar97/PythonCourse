
# %% Known issue with IPython kernel and Jypyter
# https://github.com/jupyter/notebook/issues/3397 .
import time
import asyncio
import inspect
import nest_asyncio
nest_asyncio.apply()

# %%
'''
(Co)operative (Routine) = CoRoutine

coroutine
====================
Coroutines are a more generalized form of subroutines. 
Subroutines are entered at one point and exited at another point. Coroutines can be entered, exited, and resumed at many different points. They can be implemented with the async def statement but not a requirement

coroutine function
====================
A function which returns a coroutine object. 
A coroutine function may be defined with the async def statement, and may contain await, async for, and async with keywords.

so in summary
=============
a coroutine function: an async def function;
a coroutine object: an object returned by calling a coroutine function.
https://www.youtube.com/watch?v=BI0asZuqFXM&ab_channel=sentdex
'''
# %%
async def hi():
    return 'Hi'

hi()
# Note that simply calling a coroutine will not schedule it to be executed:

# %% check the type
myVar = hi()
print(type(hi()))

# %%
print(inspect.iscoroutine(myVar))

# %% How to enumerate methods? - Use dir function
print(dir(myVar))

# Notice it has send and close method in it

# %% with await keyword
# Coroutines declared with the async/await syntax is the preferred way of writing asyncio applications.


async def myFunc():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

asyncio.run(myFunc())

# %% Note that simply calling a coroutine will not schedule it to be executed
myFunc()

# %% To actually run a coroutine, asyncio provides three main mechanisms:
# 1- The asyncio.run() function to run the top-level entry point “main()” function (see the above example.)


async def myFunc():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

asyncio.run(myFunc())

# %% 2- Awaiting on a coroutine.
#    The following snippet of code will print “hello” after waiting for 1 second, and then print “world” after waiting for another 2 seconds:


async def say_After(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")
    await say_After(1, 'hello')
    await say_After(2, 'world')
    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())

# %% 3- The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
# Let’s modify the above example and run two say_after coroutines concurrently:


async def main():
    task1 = asyncio.create_task(say_After(2, 'hello'))
    task2 = asyncio.create_task(say_After(2, 'hello'))
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())

# %%


async def echo_server():
    print('Serving on localhost:8000')
    await asyncio.start_server(handle_connection,'localhost', 8000)

async def handle_connection(reader, writer):
    print('New connection...')

    while True:
        data = await reader.read(8192)

        if not data:
            break

        print('Sending {:.10}... back'.format(repr(data)))
        writer.write(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(echo_server())
try:
    loop.run_forever()
finally:
    loop.close()
