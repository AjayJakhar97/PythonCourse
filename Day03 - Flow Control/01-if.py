#%%
if 5 > 2:
    print("Five is greater than two!")

#%%
if 5 < 2:
    print("Two is greater than five!")

# %% We can rewrite this like below
if 5 > 2:
    print("Five is greater than two!")
if 5 < 2:
    print("Two is greater than five!")

# %% or like below can rewrite this like below
if 5 > 2:
    print("Five is greater than two!")
else:
    print("Two is greater than five!")

# %% If there are multiple conditions
MyInput = 5
if 5 > MyInput:
    print("Five is greater than ", MyInput)
elif 5 == MyInput:
    print("Five is equal to ", MyInput)
else:
    print("Five is less than ", MyInput)

# %% Task 01 - Create a program to test if number is 0,+ve or -ve
number = input("Enter your number: ")

if number > 0:
    print("+ve")
elif number == 0:
    print("zero")
else:
    print("-ve")

# %% Exercise - 
'''
Given a number , for each integer in the range from 1 to n inclusive, print one value per line as follows:
Write a program that prints the numbers from 1 to 100 and for multiples of ‘3’ print “Fizz” instead of the number and for the multiples of ‘5’ print “Buzz”

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz

'''


#%% Solution

def fizzBuzz(n):
    # Write your code here
    i = 1
    while(i<n+1):
        if (i%3 == 0) and (i%5 == 0):
            print("FizzBuzz")
        elif (i%3 == 0):
            print("Fizz")
        elif (i%5 == 0):
            print("Buzz")
        else:
            print(i)
        i += 1
        
        
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)


