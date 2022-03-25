#%% You can make a function return the value that you can use later with "return" keyword

def Tip():
    return 5

Tip()

#%% Function processes result on the first return it finds and exits the call

def Tip():
    return 5
    return 6

Tip()


#%% Function processes result on the first return it finds and exits the call

def CheckOddOrEven(num):
    if num%2 == 1:
        return f"{num} is an odd number"
    else:
        return f"{num} is an even number"

print(CheckOddOrEven(2))
print(CheckOddOrEven(3))

# %% To let a function return a value with calculations, use the return statement:

def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
# %% Recursion
# Python also accepts function recursion, which means a defined function can call itself.

def my_recursion_func(k):
    if k > 0:
        result = k + my_recursion_func(k-1)
        # print(result)
    else:
        result = 0
    return result

print(my_recursion_func(5))
print("+++++++++++")

#%% If you are not careful, you can run into an infinit loop. Check below code

def recursion(x):
    while x < 10:
        sum = x + recursion(x+1)
        print(sum)
    else:
        sum = 0
    return sum

print(recursion(1))

#%% How to fix it now?

def recursion(x):
    if x <= 10:
        sum = x + recursion(x+1)
        # print(sum)
    else:
        sum = 0
    return sum

print(recursion(1))

#%% but ideally you should be mentioning the number up to which you want sum of natural numbers.
# Below is code to find the sum of natural numbers up to n using recursion

def recursion(x):
    if x >= 1:
        sum = x + recursion(x-1)
        # print(sum)
    else:
        return x
    return sum

print(recursion(10))

# %% What if you create function with name that already exists

def print():
    return False

print()

#%% Task - Calculate Total Bill with 5% tip using return statement to get tip value

def Tip(tip):
    return tip

def TotalBill(Expense,tipvar=5):
    totalTip = Expense * Tip(tipvar)/100
    print("Total Bill with tip of", totalTip, "is = ", Expense+totalTip)

TotalBill(100,10)

#%% Task01- Make use of return and print numbers from 1 to 10

def table(start = 1):
    if start <= 10:
        result = table(start+1) +1
        print(result)
    else:
        result = 0
    return result

table()
print("ended.......")

#%% Task02- Make use of return and print table of 5: 

def table(myNumber, start = 1):
    if start <= 10:
        result = table(myNumber,start + 1) + 1
        print(myNumber*result)
    else:
        result = 0
    return result

start = 1
myNumber = 5

table(myNumber)
print("ended.......")

# %% 2nd method

someNumber = 5

def table(start = 1):
    if start <= 10:
        result = 1 + table(start+1)
        # print(myNumber * result)
        print( someNumber * result)
    else:
        result = 0
    return result

table()

print("ended.......")

# %% Task01 - What do you think the result will be for the below?

someNumber = 5

def table(someNumber,start = 1):
    if start <= 10:
        result = 1 + table(start+1) # I am calling with just one argument instead of two
        print( someNumber * result)
    else:
        result = 0
    return result


table(someNumber,4)

print("ended.......")

#%% method to add two numbers

def AddTwoNumbers(x, y):
    return x+y

AddTwoNumbers(3,4)

# %% Task04 - Create your own version of absolute and print functions

def myAbs(number):
    if number > 0:
        return number
    else:
        return -number

print(myAbs(5))
print(myAbs(-5))
print(myAbs(0))
