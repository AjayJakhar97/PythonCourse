import functools

# Version 1 : Reusing Decorators
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

# Note: You can name your inner function whatever you want, and a generic name like wrapper() is usually okay.

# Version 2 : Decorating Functions With Arguments
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

# Version 3 : Returning Values From Decorated Functions
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper_do_twice

# Version 4 : Fixing introspection on Returning Values From Decorated Functions
def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper_do_twice

