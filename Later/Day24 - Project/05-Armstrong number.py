#%% Armstrong number
'''
Input: 153
return True if cubes of individual digits in the numbers is equal to the number
i.e. 1^3 + 5^3 + 3^3 = 153
'''

number = 153

def checkArmstrong(myNumber):
    original = myNumber
    remainder = 0
    sum = 0

    while myNumber > 0:
        remainder = myNumber%10
        myNumber = int(myNumber/10)
        cubeOfRemainder = remainder**3
        sum += cubeOfRemainder
        # print(remainder,cubeOfRemainder)
    return sum == original

for number in range(1000):
    if checkArmstrong(number):
        print(number)
