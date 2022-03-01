# With the while loop we can execute a set of statements as long as a condition is true.

#%% Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1


#%% Below code will keep running infinitely. So press "Ctrl + c" to stop it
i = 1
while i == 1:
    print(i, "- Hello again...")
    i = i+1  # 1 + 1
    print("The current value of i is ", i)

# The break Statement
# ========================
# With the break statement we can stop the loop even if the while condition is true
#%% Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# The continue Statement
# =========================
# With the continue statement we can stop the current iteration, and continue with the next:
#%% Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# The else Statement
# ============================
# With the else statement we can run a block of code once when the condition no longer is true:

#%% Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#%% Make sure you know how to find modulus for next exercise 

print(3%1)
print(3%2)
print(3%3)

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


#%% 

x = 3
y = 0

while y < x:
    print(y+1)
    y = y + 1

# %%
