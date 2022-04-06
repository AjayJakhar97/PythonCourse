'''
Python Try Except
====================
1- The try block lets you test a block of code for errors.
2- The except block lets you handle the error.
3- The else block lets you execute code when there is no error.
4- The finally block lets you execute code, regardless of the result of the try- and except blocks.

Exception Handling
====================
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement:
'''

#%% Example : The try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")

#%% This statement will raise an error, because x is not defined:

'''Since the try block raises an error, the except block will be executed.
Without the try block, the program will crash and raise an error:

'''
print(x)

#%% Many Exceptions
'''You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

Example
Print one message if the try block raises a NameError and another for other errors:
'''
# x = "something"
try:
    # print(x)
    x+5
except NameError:
    print("Not defined")
except:
    print("something else went wrong")

#%% Else
'''You can use the else keyword to define a block of code to be executed if no errors were raised:

Example
In this example, the try block does not generate any error:
'''
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#%% Finally
'''The finally block, if specified, will be executed regardless if the try block raises an error or not.
'''
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

#%% This can be useful to close objects and clean up resources:

# Try to open and write to a file that is not writable:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# The program can continue, without leaving the file object open.

#%% Raise an exception
'''As a Python developer you can choose to throw an exception if a condition occurs.
To throw (or raise) an exception, use the raise keyword.

Example
Raise an error and stop the program if x is lower than 0:
'''
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

#%% The raise keyword is used to raise an exception.
'''
You can define what kind of error to raise, and the text to print to the user.

Example
Raise a TypeError if x is not an integer:
'''
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")


# %% Task 01 - Create a program to test if number is 0,+ve or -ve

number = input("Enter your number: ")
try:
    int(number)
    # number = int(number)
    if number > 0:
        print("+ve")
    elif number == 0:
        print("zero")
    elif number < 0:
        print("-ve")
except:
    print("Invalid Input")

#%% Below shows built-in exceptions that are usually raised in Python

try:
  # 2 + "2"
  2/0
  2
except ArithmeticError:
  print("ArithmeticError exception. It includes 'OverFlowError', 'ZeroDivisionError' and 'FloatingPointError'")
except AssertionError:
  print("Assertion Error")
except AttributeError:
  print("Attribute Error")
# except Exception:
#   print("Exception")
except EOFError:
  print("EOF Error")
except FloatingPointError:
  print("Floating Point Error")
except GeneratorExit:
  print("Generator Exit")
except ImportError:
  print("Import Error")
except IndentationError:
  print("Indentation Error")
except IndexError:
  print("Index Error")
except KeyError:
  print("Key Error")
except KeyboardInterrupt:
  print("Keyboard Interrupt")
except LookupError:
  print("Lookup Error")
except MemoryError:
  print("Memory Error")
except NameError:
  print("Name Error")
except NotImplementedError:
  print("Not Implemented Error")
except OSError:
  print("OS Error")
except OverflowError:
  print("Overflow Error")
except ReferenceError:
  print("Reference Error")
except RuntimeError:
  print("Runtime Error")
except StopIteration:
  print("Stop Iteration")
except SyntaxError:
  print("Syntax Error")
except TabError:
  print("Tab Error")
except SystemError:
  print("System Error")
except SystemExit:
  print("System Exit")
except TypeError:
  print("Type Error")
except UnboundLocalError:
  print("Unbound Local Error")
except UnicodeError:
  print("Unicode Error")
except UnicodeEncodeError:
  print("Unicode Encode Error")
except UnicodeDecodeError:
  print("Unicode Decode Error")
except UnicodeTranslateError:
  print("Unicode Translate Error")
except ValueError:
  print("Value Error")
except ZeroDivisionError:
  print("Zero Division Error")
except Exception:
  print("Some other error")

#%% Exception hierarchy
'''
Exception hierarchy
The class hierarchy for built-in exceptions is:

BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- EncodingWarning
           +-- ResourceWarning


'''
# %% ArithmeticError exception
'''
BaseException
 +-- Exception
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
'''
import math

try:
  # 1 : OverflowError : # In Python, OverflowError occurs when any operations like arithmetic operations or any other variable storing any value above its limit then there occurs an overflow of values that will exceed it’s specified or already defined limit. 
  print(math.exp(1000))

  # 2 : FloatingPointError : Doesn't occur any more. More Info on https://python.readthedocs.io/en/latest/library/fpectl.html

  # 3 : ZeroDivisionError : # In Python, ZeroDivisionError occurs when any division operation or any other variable storing any value as zero then there occurs an division by zero error.
  print(5/0)

except OverflowError:
  print("Overflow Error")
except FloatingPointError:
  print("Floating Point Error")
except ZeroDivisionError:
  print("Zero Division Error")
except ArithmeticError:
  print("ArithmeticError exception. It includes 'OverFlowError', 'ZeroDivisionError' and 'FloatingPointError'")

#%% indentation error
# Note: Syntax error should not be handle through exception handling it should be fixed in your code.

'''
# https://stackoverflow.com/questions/8911735/how-to-catch-indentationerror

BaseException
 +-- Exception
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError

IndentationError is raised when the module is compiled. You can catch it when importing a module, since the module will be compiled on first import. You can't catch it in the same module that contains the try/except, because with the IndentationError, Python won't be able to finish compiling the module, and no code in the module will be run.

So below won't work...

try:

  def f():
    z=['foo','bar']
    for i in z:
      if i == 'foo':
      pass
except IndentationError:
  print("Indentation Error")

print("Done...")
'''
try:
  import test
except IndentationError:
  print("Indentation Error")

print("Done...")

# Reference : https://www.datacamp.com/community/tutorials/exception-handling-python

#%% TabError

try:
  import test
except TabError:
  print("Tab Error")

print("Done...")
