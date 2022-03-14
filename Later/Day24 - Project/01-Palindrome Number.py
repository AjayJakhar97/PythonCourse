# %% Palindrome Number
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is a palindrome while 123 is not.

# Given an integer x, return true if x is palindrome integer.
# reference: https://leetcode.com/problems/palindrome-number/

from random import triangular


def palindromeCheck(num):
    num = str(num)

    # for item in x:
    #     print(item)

    for i in range(int(len(num)/2)):
        if num[i] == num[len(num)-(i+1)]:
            return True
        else:
            return False


palindromeCheck(121)
palindromeCheck(-121)
palindromeCheck(10)


# %% Follow up: Could you solve it without converting the integer to a string?

def palindromeCheck(num):
    x, y = num, 0
    f = lambda: (y * 10) + x % 10
    while x > 0:
        x, y = x//10 , f()
    return y == num
           

palindromeCheck(121)
palindromeCheck(-121)
palindromeCheck(10)
